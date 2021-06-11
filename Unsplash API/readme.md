## Unsplash API

- api_call.py downloads a random image from Unsplash and saves it in an S3 bucket. Image information is stored in json format in a separate folder
- lambda_function.py executes api_call.py
- json_to_dynamo_db.py is triggered as soon as a json file is added to the S3 bucket and uploads the files to DynamoDB
