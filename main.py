import boto3
# from botocore.exceptions import ClientError
from dotenv import load_dotenv
import sqlite3
import os

# Load .env
load_dotenv()
# Create database connection
# db = sqlite3.connect('instances.db')

# Make the connection
ec2 = boto3.client('ec2',
                   aws_access_key_id=os.getenv('AWS_ID'),
                   aws_secret_access_key=os.getenv('AWS_SECRET'),
                   region_name=os.getenv('AWS_REGION'))

# Get list of instances
response = ec2.describe_instances()

reservations = response['Reservations']

for reserve in reservations:
    instance = reserve['Instances'][0]
    # print(instance)
    print(instance['Tags'][0]['Value'],' - ', instance['InstanceId'],' [', instance['State']['Name'], ']')

# db.close()