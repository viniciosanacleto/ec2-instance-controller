import boto3
from botocore.exceptions import ClientError

key_id='xxxxxx'
key_secret='xxxxxx'
region='xxxxxx'

ec2 = boto3.client('ec2',aws_access_key_id=key_id, aws_secret_access_key=key_secret, region_name=region)

instance_list = ec2.describe_instances(InstanceIds=['i-01d39373421e303a8'])

if instance_list:
	try:
		ec2.stop_instances(InstanceIds=['i-01d39373421e303a8'])
	except ClientError as e:
		print("ERROR: ",e)
