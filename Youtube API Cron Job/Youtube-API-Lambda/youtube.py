import json
import requests
from datetime import date
from datetime import datetime
import csv
import boto3

class YTstats:

    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_name = None
        self.channel_statistics = None

    def get_channel_title(self):
        """Get the channel name."""

        url_title = f'https://www.googleapis.com/youtube/v3/channels?part=snippet&id={self.channel_id}&key={self.api_key}'

        json_url_title = requests.get(url_title)
        channel_name_json = json.loads(json_url_title.text)
        channel_name_json = channel_name_json['items'][0]['snippet']['title']

        self.channel_name = channel_name_json
        return channel_name_json

    def get_channel_statistics(self):
        """Extract the channel statistics"""

        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}'

        json_url = requests.get(url)
        statistics = json.loads(json_url.text)
        statistics = statistics['items'][0]

        self.channel_statistics = statistics
        return statistics

    def to_csv_channel(self):
        """Saves the channel statistics to a csv file.
        Args:
            csv_directory: file path and  file name
        """
        
        s3 = boto3.client('s3')

        date_col = datetime.now()
        date_col_new = datetime.strftime(date_col, '%Y-%m-%d_%H:%M:%S')
        dt = datetime.strftime(date_col, '%Y-%m-%d')
        self.get_channel_title()
        channel = self.channel_name.replace(' ', '_')
        channel_id = self.channel_statistics['id']
        views = self.channel_statistics['statistics']['viewCount']
        subscribers = self.channel_statistics['statistics']['subscriberCount']
        videos = self.channel_statistics['statistics']['videoCount']
        
        final_file_name='youtube-api/youtube_'+ dt +'.csv' # includes the folder which sits in the destination bucket
        bucket = 'destination_bucket'
        
        with open('/tmp/youtube.csv', 'a', newline = '') as csvfile:
            fieldnames = ['date', 'channel_id', 'channel', 'views', 'subscribers', 'videos']

            writer = csv.DictWriter(csvfile, fieldnames = fieldnames, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)

            # Writes headers only once
            if csvfile.tell() == 0:
                writer.writeheader()

            # Append data to existing csv file
            writer.writerow({'date': date_col_new, 'channel_id': channel_id, 'channel': channel,
                             'views': views, 'subscribers': subscribers, 'videos': videos})
                             
        s3.upload_file('/tmp/youtube.csv', Bucket = bucket, Key = final_file_name)