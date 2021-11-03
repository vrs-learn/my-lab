import botocore, boto3

def create_instance():
    ec2_client = boto3.client("ec2", region_name="ap-south-1")
    instances = ec2_client.run_instances(
        ImageId="ami-0ad704c126371a549",
        MinCount=1,
        MaxCount=2,
        InstanceType="t2.micro",
        KeyName="ec2-key"
    )
    print(instances)
    #print(instances["Instances"][0]["InstanceId"])

create_instance()