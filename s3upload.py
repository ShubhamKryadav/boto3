import boto3
s3 = boto3.resource('s3')
s3.meta.client.upload_file(r"C:\Users\DESKTOP\Desktop\java\python\boto3\hello.txt" , 'shubhambucket29', 'hello.txt')
