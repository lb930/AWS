import requests
import json
import os
import boto3

class UnsplashAPI:

    def get_images(self, orientation: str, *topics: list):
        '''
        Parameters:
            orientation: image orientation: landscape,  portrait or squarish
            topics: image topics; if multiple: comma separated
        Returns:
            json output with image data
        '''

        try:
            t = ','.join(*topics)
            access_key = os.environ['unsplash_access']
            response = requests.get('https://api.unsplash.com/photos/random?client_id=' + access_key + '&orientation=' + orientation + '&topic=' + t)
            
            # Only needed to investigate json structure
            # investigate = json.dumps(response.json(), sort_keys=True, indent=4)
            # print(investigate)
            
            self.data = response.json()
            return self.data
            
        except Exception as err:
            raise

    def download_image(self):
        '''Downloads random image to S3'''
        
        bucket = 'unsplash-api'

        try:
            s3 = boto3.client('s3')
            image_url = requests.get(self.data['urls']['small'])
            
            image = image_url.content
            img_descr = self.data['alt_description']
            img_name = self.data['id']
            img_url = 'https://unsplash.com/photos/' + img_name
            
            # Save jpeg
            lambda_path = '/tmp/' + img_name + '.jpg'
            with open(lambda_path, 'wb') as f:
                f.write(image)
            s3.upload_file(lambda_path, Bucket = bucket, Key = 'images/' + img_name + '.jpg')
            
            # Save json file
            lambda_path_json = '/tmp/' + img_name + '.json'
            with open(lambda_path_json, 'w') as fp:
                json.dump(self.data, fp)
            s3.upload_file(lambda_path_json, Bucket = bucket, Key = 'json_files/' + img_name + '.json')
            
            print(img_descr)
            print(f'{img_name} downloaded: {img_url}')
        
        except Exception as err:
            raise