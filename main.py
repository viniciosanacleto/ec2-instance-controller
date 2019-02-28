import boto3
# from botocore.exceptions import ClientError
from dotenv import load_dotenv
import sqlite3
import os

# Load .env
load_dotenv()
# Create database connection
db = sqlite3.connect('instances.db')

# Make the connection
# ec2 = boto3.client('ec2',
#                    aws_access_key_id=os.getenv('AWS_ID'),
#                    aws_secret_access_key=os.getenv('AWS_SECRET'),
#                    region_name=os.getenv('AWS_REGION'))

# Get list of instances
# instance_list = ec2.describe_instances


db.close()