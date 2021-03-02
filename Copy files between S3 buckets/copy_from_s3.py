import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    err = None
    
    # source bucket
    bucket = event['Records'][0]['s3']['bucket']['name'] 

    # source folder and file
    key = event['Records'][0]['s3']['object']['key']

    # source file without the folder
    key_file = key.split('/')[1]
    
    destination_bucket = 'your_destination_bucket'

    # Bucket and Key: destination bucket and destination file
    try:
        s3_client.copy_object(Bucket=destination_bucket, Key=key_file, CopySource={
                              'Bucket': bucket, 'Key': key})
        
        # delete object from source bucket
        s3_client.delete_object(Bucket = bucket, Key = key)

    except Exception as e:
        err = str(e)

    return {
        'status': 500 if err else 200,
        'error': err
    }