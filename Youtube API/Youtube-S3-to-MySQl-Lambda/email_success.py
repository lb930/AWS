import boto3

ses = boto3.client('ses')

email_from = 'your_email'
email_to = 'your_email'
email_subject = 'Data uploaded successfully'
email_body = 'Data was successfully uploaded to MySQL database.'


def email_success_func():
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
                    'Data': email_body
                }
            }
        }
    )
