import base64, boto3, random, requests, time
from PIL import Image, ImageFilter
from io import BytesIO

rek     = boto3.client("rekognition")

def get_face_boxes(faces, source_size):
    return [
        (
            int(f['BoundingBox']['Left'] * source_size[0]),
            int(f['BoundingBox']['Top'] * source_size[1]),
            int((f['BoundingBox']['Left'] + f['BoundingBox']['Width']) * source_size[0]),
            int((f['BoundingBox']['Top'] + f['BoundingBox']['Height']) * source_size[1]),
            f['Pose']['Roll']
        )
        for f in faces
    ]

def blur_faces(x):
    im          = Image.open(x)
    source_size = im.size[0], im.size[1]
    im.seek(0)
 
    resp        = rek.detect_faces(Image={"Bytes": x.getvalue()})   
    faces       = [face for face in resp['FaceDetails'] if face['Confidence'] > 80]

    for face_box in get_face_boxes(faces, source_size):
        face_img        = im.copy()
        blurred_face    = face_img.crop(face_box[:4])
        blurred_face    = blurred_face.filter(ImageFilter.GaussianBlur(20))
        im.paste(blurred_face, (face_box[0], face_box[1]))

    b       = BytesIO()
    im.save(b, format = "JPEG")
    b64     = base64.b64encode(b.getvalue())

    return b, b64

# returns a binary representation of the image plus a base64 string
def download(fimg):
    r       = requests.get(fimg)
    im 	    = Image.open(BytesIO(r.content))

    b       = BytesIO()
    im.save(b, format = "JPEG")
    
    b64     = base64.b64encode(b.getvalue())
    return b, b64

def handler(event, context):
    startt  = int(round(time.time() * 1000))

    f_img           = 'https://loremflickr.com/800/600/smile?lock='+str(random.randint(1, 10000))
    s_img, s_b64    = download(f_img)
    n_img, n_b64    = blur_faces(s_img)
    endt            = int(round(time.time() * 1000))
    
    h               = '<html><head>'+open('main.css').read()+'</head>'
    h               += '<body><center><br><h2>Serverless blurring service</h2></center>'
    h               += '<table align = "center" width = "1000" cellpadding = "10"><tr><td colspan = "2">This webpage picks a random image from loremflickr.com, finds faces using the Rekognition service in the picture and blurs them. You can download the sourcecode from <a href = "https://github.com/marekq/lambda-image-blur">GitHub</a> or deploy the application through the <a href="https://serverlessrepo.aws.amazon.com/#/applications/arn:aws:serverlessrepo:us-east-1:517266833056:applications~lambda-image-blur">Serverless Application Repository</a>.</td></tr><tr><td><b>original image</b></td><td><b>blurred image</b></td></tr><tr>'
    h               += '<td><img src="data:image/jpg;base64,'+str(s_b64.decode('utf8'))+'"></td>'
    h               += '<td><img src="data:image/jpg;base64,'+str(n_b64.decode('utf8'))+'"></td>'
    h               += '</tr><td colspan = "2"><br>The original image can be found at <a href = "'+f_img+'">'+f_img+'</a> and has a Creative Commons license. The blurring process took '+str(endt - startt)+' miliseconds.</td></body></html>'
    
    return {'statusCode': '200',
		'body': str(h),
		'headers': {'Content-Type': 'text/html', 'charset': 'utf-8'}} 