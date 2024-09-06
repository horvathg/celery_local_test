import boto3, json

# Set up the SQS client to use LocalStack
sqs = boto3.client('sqs', endpoint_url='http://localhost:4566', region_name='us-east-1')

# List SQS queues to ensure connection is working
response = sqs.list_queues()
print(json.dumps(response.get('QueueUrls', [])))
