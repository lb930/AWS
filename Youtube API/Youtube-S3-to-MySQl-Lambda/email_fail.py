import boto3

ses = boto3.client('ses')

email_from = 'your_email'
email_to = 'your_email'
email_subject = 'Data upload failed'


def email_fail_func(error):
    response = ses.send_email(
        Source = email_from,
        Destination={
            'ToAddresses': [
                email_to,
            ]
        },
        Message={
            'Subject': {
                'Data': email_subject
            },
            'Body': {
                'Text': {
                    'Data': error
                }
            }
        }
    )
