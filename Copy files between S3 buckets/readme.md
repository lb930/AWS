# Move Files between S3 folders

Use the boto3 copy_object() and delete_object() method to move files between S3 buckets.

## Folder Structure

Source bucket
&nbsp;+-- Source folder
&nbsp;&nbsp;&nbsp;&nbsp;+-- Source files

Destination bucket
&nbsp;+-- Destination file