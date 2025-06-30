import boto3
from botocore.exceptions import ClientError

# Set your region and bucket name
region = "ap-south-1"  # Mumbai
bucket_name = "my-unique-bucket-123456789"  # Bucket name must be globally unique

# Create S3 client
s3 = boto3.client('s3', region_name=region)

try:
    # Create the S3 bucket
    if region == "us-east-1":
        response = s3.create_bucket(Bucket=bucket_name)
    else:
        response = s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region}
        )
    print(f"✅ Bucket '{bucket_name}' created successfully!")
except ClientError as e:
    print(f"❌ Error creating bucket: {e}")
