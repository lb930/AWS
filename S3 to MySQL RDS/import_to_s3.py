import boto3 
import os

access_key = os.environ.get('AWS_ACCESS_KEY_ID')
secret_access = os.environ.get('AWS_SECRET_ACCESS_KEY_ID')

s3_client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_access)

for file in os.listdir():
    if '.csv' in file:
        upload_file_bucket = 'firstawsbuckettest'
        upload_file_key = 'csvdata/' + str(file)
        s3_client.upload_file(file, upload_file_bucket, upload_file_key)

        print(f'{file} uploaded successfully')
