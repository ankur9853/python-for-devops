# List
# A list is a collection of items that are ordered and changeable. Lists are written with square brackets [].

s3_bucket_list = ["bucket1", "bucket2", "bucket3"]
print(type(s3_bucket_list))
print("S3 bucket list:", s3_bucket_list)

s3_bucket_list.append("bucket4")
print("S3 bucket list after appending:", s3_bucket_list)

s3_bucket_list.remove("bucket2")
print("S3 bucket list after removing:", s3_bucket_list)

s3_bucket_list[0] = "new_bucket1"
print("S3 bucket list after updating:", s3_bucket_list)

s3_bucket_list.__len__() # this will give the length of the list
print("Length of S3 bucket list:", s3_bucket_list.__len__())

s3_bucket_list.sort() # this will sort the list in ascending order
print("S3 bucket list after sorting:", s3_bucket_list)

print("S3 bucket list in reverse order:", s3_bucket_list[::-1]) # this will give the list in reverse order

print("S3 bucket list in reverse order using reverse method:", s3_bucket_list.reverse()) # this will reverse the list in place

print("S3 bucket list after reversing:", s3_bucket_list)

print("S3 bucket list with new bucket:", s3_bucket_list + ["new_bucket4"]) #concatenate bucket with new bucket.
