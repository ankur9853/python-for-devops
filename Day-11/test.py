#list of dictionaries

ec2_instances_info  = [
    {
        "instance_id": "i-1234567890abcdef0",
        "instance_type": "t2.micro",
        "region": "us-east-1"
    },
    {
        "instance_id": "i-01234567890abcdef1",
        "instance_type": "t2.small",
        "region": "us-west-2"
    },  
    {
        "instance_id": "i-abcdef01234567890",
        "instance_type": "t2.medium",
        "region": "eu-west-1"
    }
]

print(ec2_instances_info[1]["region"])