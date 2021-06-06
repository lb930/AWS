import boto3
import json

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    
    err = None
    
    # source bucket
    bucket = event['Records'][0]['s3']['bucket']['name'] 
    
    # source folder and file
    key = event['Records'][0]['s3']['object']['key']
    
    print(bucket)
    print(key)
    
    try:
    
        json_object = s3_client.get_object(Bucket=bucket,Key=key)
        jsonFileReader = json_object['Body'].read()
        jsonDict = json.loads(jsonFileReader)
        table = dynamodb.Table('unsplash')
        table.put_item(Item=jsonDict)
        
    except Exception as e:
        err = str(e)
        
    return {
        'statusCode': 200,
    }
