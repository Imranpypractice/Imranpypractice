import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')  # Change region if needed

# Launch EC2 instance
response = ec2.run_instances(
    ImageId='ami-05ffe3c48a9991133',      # ✅ Replace with your desired AMI ID
    InstanceType='t2.micro',              # ✅ Choose the desired instance type
    KeyName='pkey.pem',                # ✅ Replace with your existing Key Pair name
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=['sg-03720ce8289b4596b'],  # ✅ Replace with your Security Group ID
    SubnetId='subnet-0fe7f885463e4dfa7',        # ✅ Replace with your Subnet ID
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'MyEC2Instance'}]
        }
    ]
)

# Output instance ID
instance_id = response['Instances'][0]['InstanceId']
print(f"EC2 Instance Created with ID: {instance_id}")
