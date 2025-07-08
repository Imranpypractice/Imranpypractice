import boto3

s3 = boto3.client('s3', region_name='us-east-1')

bucket_name = 'my-emranbucket12345678'

s3.create_bucket(Bucket=bucket_name)  # ✅ No LocationConstraint for us-east-1
