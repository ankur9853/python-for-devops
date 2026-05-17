import boto3
# explain below code
# The code imports the boto3 library, which is the Amazon Web Services (AWS) SDK

client = boto3.client('s3') #why do we need to create a client for s3?
# We need to create a client for S3 (Simple Storage Service) in order to interact
#response = client.create_bucket(
#    Bucket='meethi-first-bucket1-1234567890',
#    CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'}
#)

response = client.delete_bucket(
    #delete all bucket started with name meethi.
    Bucket='meethi-first-bucket1-1234567890',
    #ExpectedBucketOwner='string'
)



#response = client.get_bucket_acl(
#    Bucket='meethi-first-bucket-1234567890-1234567890-1234567890-1234567890',
#    #ExpectedBucketOwner='string'
#)

#print(response)