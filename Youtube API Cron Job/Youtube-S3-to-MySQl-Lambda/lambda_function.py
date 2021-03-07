import boto3
import csv
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    
    date_col = datetime.now()
    dt = datetime.strftime(date_col, '%Y-%m-%d')

    result = []

    bucket = 'bucket_withyoutube_csv_file'
    csv_file = 'youtube-api/youtube_'+ dt +'.csv'
    csv_file_obj = s3_client.get_object(Bucket=bucket, Key=csv_file)
    lines = csv_file_obj['Body'].read().decode('utf-8').split()

    for row in csv.DictReader(lines):
        result.append(row.values())

    try:
        connection = mysql.connector.connect(host='your_aws_database_host', 
                                            database='databse_name_in_MySQL', 
                                            user='your_username',
                                            password='your_password')
                                            
        mysql_empsql_insert_query = "INSERT INTO youtube (date_col, channel_id, channel_name, views, subscribers, videos)    VALUES (%s, %s, %s, %s, %s, %s)"

        cursor = connection.cursor()
        cursor.executemany(mysql_empsql_insert_query, result)
        connection.commit()
        print(cursor.rowcount, "record(s) inserted successfully into test table")

    
    except Exception as err:
        print ("Error -"+str(err))
        
    return {'statusCode': 200}
