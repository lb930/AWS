import json
import boto3
import csv
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    print(event) # this is used to determine the JSON structure for bucket and csv_file below
    result = []

    # Fetch object from S3
    bucket = event['Records'][0]['s3']['bucket']['name']
    csv_file = event['Records'][0]['s3']['object']['key']
    csv_file_obj = s3_client.get_object(Bucket=bucket, Key=csv_file)

    # Read in rows
    lines = csv_file_obj['Body'].read().decode('utf-8').split()
    for row in csv.DictReader(lines):
        result.append(row.values())
    
    try:
        # Connect to DBS
        connection = mysql.connector.connect(host='your_aws_database_host', 
                                            database='databse_name_in_MySQL', 
                                            user='admin',
                                            password='your_password')
                                            
        # Insert data
        mysql_empsql_insert_query = "INSERT INTO test (text_col, number_col, date_col)    VALUES (%s, %s, %s)"
        cursor = connection.cursor()
        cursor.executemany(mysql_empsql_insert_query, result)
        connection.commit()
        print(cursor.rowcount, "record(s) inserted successfully into table")

    except Exception as err:
        print ("Error -"+str(err))

    return {'statusCode': 200, 'body': json.dumps('Hello from Lambda')}
