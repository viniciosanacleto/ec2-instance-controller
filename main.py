import boto3
# from botocore.exceptions import ClientError
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Make the connection
ec2 = boto3.client('ec2',
                   aws_access_key_id=os.getenv('AWS_ID'),
                   aws_secret_access_key=os.getenv('AWS_SECRET'),
                   region_name=os.getenv('AWS_REGION'))


