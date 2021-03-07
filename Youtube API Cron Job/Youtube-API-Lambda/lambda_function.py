from key import api_key_str
from youtube import YTstats

def lambda_handler(event, context):

    key = api_key_str

    channel_ids = ['channel_id_from_the_channel_URL']

    for id in channel_ids:
        yt = YTstats(key, id)
        yt.get_channel_statistics()
        yt.to_csv_channel()

    return {
        'statusCode': 200,
    }