import boto3
s3 = boto3.resource('s3')
ec2 = boto3.resource('ec2')
stat = boto3.Session('ec2')
print(s3.buckets.all())
print(ec2)
print(stat)

#Creating an instance

instances = ec2.create_instances(
    ImageId="ami-0989fb15ce71ba39e",
    MinCount=1,
    MaxCount=1,
    InstanceType='t3.micro',
    KeyName='rac007'
)