import boto3 
import os
import pandas as pd

class DownloadFromS3:

    def parameters(self):

        self.access_key = os.environ.get('AWS_ACCESS_KEY_ID')
        self.secret_access = os.environ.get('AWS_SECRET_ACCESS_KEY_ID')
        self.bucket = 'unsplash-api-bucket'
        self.storage_dir = os.getcwd() + '\\'

        return self.access_key, self.secret_access, self.bucket, self.storage_dir

    def connect_to_S3(self):
        s3_client = boto3.client('s3', aws_access_key_id = self.access_key, aws_secret_access_key = self.secret_access)

        # Get all files in images folder
        self.bucket_content = s3_client.list_objects_v2(Bucket=self.bucket, Prefix='images/')

        return self.bucket_content

    def get_latest_upload(self):
        data = []

        # iterate over all keys in bucket (= number of items)
        for item in range(1, self.bucket_content['KeyCount']):
            data.append([self.bucket_content['Contents'][item]['Key'], self.bucket_content['Contents'][item]['LastModified']])

        # turn list into df and sort descending by date to get latest item
        df = pd.DataFrame(data, columns=["item_name", "upload_date"])
        df.sort_values(by=['upload_date'], inplace = True, ascending = False)
        df = df.head(1)
        self.download_item = df.iloc[0,0]
        self.item_name = self.download_item.split('/')[1]
        print(f'Prefix and item: {self.download_item}')
        print(f'Item: {self.item_name}')

        return self.download_item, self.item_name

    def download_item_from_S3(self):

        # Download file to specific folder
        s3 = boto3.resource('s3', aws_access_key_id = self.access_key, aws_secret_access_key = self.secret_access)
        s3.Bucket(self.bucket).download_file(self.download_item, self.storage_dir + self.item_name)

if __name__ == '__main__':
    s = DownloadFromS3()
    s.parameters()
    s.connect_to_S3()
    s.get_latest_upload()
    s.download_item_from_S3()