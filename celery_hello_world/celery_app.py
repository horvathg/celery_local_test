from celery import Celery
import os

# Create a Celery application instance
celery_app = Celery('celery_hello_world',
                    broker='sqs://',
                    backend='rpc://'
                    )

aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

broker_url = "sqs://{aws_access_key}:{aws_secret_key}@localhost:4566".format(
    aws_access_key=aws_access_key, aws_secret_key=aws_secret_key,
)

celery_app.conf.update(
    broker_transport_options={
    'region': 'us-east-1',  # Specify your AWS region
    'predefined_queues': {
        'localstack-celery': {
            'url': 'http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/localstack-celery',
            'access_key_id':'dummy_access_key',
            'secret_access_key':'dummy_secret_key',
        }
    },
    'polling_interval': 5.0,  # Adjust polling interval as needed
    'wait_time_seconds': 20,  # Use long polling
    'visibility_timeout': 3600,  # Set visibility timeout (optional)
    },
    broker_url=broker_url,
    task_default_queue='localstack-celery',
    aws_access_key_id='dummy_access_key',
    aws_secret_access_key='dummy_secret_key',
)
