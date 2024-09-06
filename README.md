# Usage

## prerequisites

1. `docker run --rm -p 4566:4566 -p 4571:4571 -d localstack/localstack`
2. `aws --endpoint-url=http://localhost:4566 sqs create-queue --queue-name localstack-celery --region us-east-1`

1. `source .env`
2. `celery -A celery_hello_world.celery_app worker --loglevel=info`
3. `python main.py`
