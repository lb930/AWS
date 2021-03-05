# Move Files between S3 folders and deploy infrastructure with Terraform

Use the boto3 ```copy_object()``` and ```delete_object()``` method to move files between S3 buckets.

## Folder Structure
```bash
├── Source bucket (terraform-luisa)
    ├── Source files

├── Destination bucket (backup-bucket-luisa)
    ├── Destination file
```

## Terraform files

### main.tf

This file creates the bucket that we'll use as a source to move files into a destination bucket. Public access has been denied.

### lambda_iam.tf

Creates a role for our lambda function and gives it full access to S3 and CloudWatch.

### lambda.tf

- locals: Creates an output path for the zip file.

- archive_file: Creates a zip file of the Python script that we want to use in our lambda function.

- aws_lambda_permission: Gives an external source (here: S3) permission to access the Lambda function.

- aws_lambda_function: assigns a role and the Python script to the Lambda function. It also ensures that an updated Python function gets pushed to AWS

- aws_s3_bucket_notification: Creates a trigger


