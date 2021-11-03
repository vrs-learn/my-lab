import boto3, os

import botocore

service = "ec2"
region = "ap-south-1"
image_id = "ami-0ad704c126371a549"

outfile = open('ec2-key.pem','w')
ec2_client = boto3.client('ec2')

try: 
    key_pair = ec2_client.create_key_pair(KeyName = "ec2-key")
    key_pair_out = str(key_pair["KeyMaterial"])
    print(key_pair)
    outfile.write(key_pair_out)
except botocore.exceptions.ClientError as e:
    print("Key already exists" + str(e))
except :
    print("Some error occured.")




