import boto3
import os, sys, stat
import json
ec2 = boto3.resource('ec2','us-east-1')



# create a file to store the key locally
outfile = open('ec2-keypair.pem','w')
# call the boto ec2 function to create a key pair
key_pair = ec2.create_key_pair(KeyName='ec2-keypair')
# capture the key and store it in a file
KeyPairOut = str(key_pair.key_material)
outfile.write(KeyPairOut)
os.chmod("ec2-keypair.pem",  0o444)

inst_info={}


def create_instance_ec2(inst_type="t2.micro",ami_id="ami-00b6a8a2bd28daf19",region="us-east-1",KeypairName="ec2-keypair"):
# create a new EC2 instance
    instances = ec2.create_instances(
        ImageId=ami_id,
        MinCount=1,
        MaxCount=2,
       InstanceType=inst_type,
       KeyName=KeypairName
    )
    inst_info['instance_id']=instance[0].id
    inst_info['public_ip']=instance[0].public_ip_address
    #instances.start()

    return json.dumps(inst_info)

if __name__ == '__main__':
    create_instance_ec2()

