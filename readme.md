lambda-image-blur
=================


A demopage to demonstrate how faces in pictures can be blurred using Amazon Rekognition. You will have access to your own blurring service running behind an API Gateway which you can use as a base for your own anonymizing solution. A demo of the solution can be found here; [https://blur.marek.host](https://blur.marek.host)


![alt tag](https://raw.githubusercontent.com/marekq/lambda-image-blur/master/docs/1.png)


Installation
------------


The simplest way to deploy the demo application is through the [Serverless Application Repository](https://serverlessrepo.aws.amazon.com/#/applications/arn:aws:serverlessrepo:us-east-1:517266833056:applications~lambda-image-blur). After about a minute or so, the HTTPS endpoint to visit the service will be live. 

For a manual installation - run install.sh in the Lambda directory first to download the Python Imaging Library (PIL). Next, make a zip file of the full folder. Finally, deploy the attached SAM template through the CloudFormation console or CLI.  


Contact
-------

In case of questions or bugs, please raise an issue or reach out to @marekq!

