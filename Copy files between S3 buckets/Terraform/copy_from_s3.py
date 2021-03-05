import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    err = None
    
    # source bucket
    bucket = event['Records'][0]['s3']['bucket']['name'] 

    # source folder and file
    key = event['Records'][0]['s3']['object']['key']
    destination_bucket = 'backup-bucket-luisa'

    # Bucket and Key: destination bucket and folder 
    try:
        s3_client.copy_object(Bucket=destination_bucket, Key=key, CopySource={
                              'Bucket': bucket, 'Key': key})
        # delete object from source bucket
        s3_client.delete_object(Bucket = bucket, Key = key)

    except Exception as e:
        err = str(e)

    return {
        'status': 500 if err else 200,
        'error': err
    }