from api_call import UnsplashAPI

def lambda_handler(event, context):
    u = UnsplashAPI()
    u.get_images('landscape', ['nature'])
    u.download_image()
    
    return {
        'statusCode': 200,
    }
