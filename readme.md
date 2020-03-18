lambda-image-blur
=================


A demopage to demonstrate how faces in pictures can be blurred using Amazon Rekognition. You will have access to your own blurring service running behind an API Gateway which you can use as a base for your own anonymizing solution. A demo of the solution can be found here; [https://blur.marek.host](https://blur.marek.host)


![alt tag](https://raw.githubusercontent.com/marekq/lambda-image-blur/master/docs/1.png)


Installation
------------


The simplest way to deploy the demo application is through the [Serverless Application Repository](https://serverlessrepo.aws.amazon.com/#/applications/arn:aws:serverlessrepo:us-east-1:517266833056:applications~lambda-image-blur). After about a minute or so, the HTTPS endpoint to visit the service will be live and you can visit the page. 

For a manual installation, you need to have the AWS SAM CLI installed and Docker running on your machine. Next, run deploy.sh in the Lambda directory to build the Lambda artifact and deploy using AWS SAM. During the process, you will be asked to specify the region that you want to deploy to. Finally you will be presented with the web URL where you can view the page. 


Contact
-------

In case of questions or bugs, please raise an issue or reach out to @marekq!

