import boto3
client = boto3.client('ec2')
response = client.stop_instances(
    InstanceIds=[
        'i-06ede22472f69b87c',
    ]
)
