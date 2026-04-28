# Tuple
# Tuples are immutable, which means that once a tuple is created, it cannot be modified. Tuples are defined using parentheses () 
# and can contain any number of elements, including duplicates.

s3_bucket_tuple = ("bucket1", "bucket2", "bucket3")
print(type(s3_bucket_tuple))
print(s3_bucket_tuple)

s3_bucket_tuple.count("bucket2") # this will give the count of "bucket2" in the tuple  
print("Count of bucket2 in the tuple:", s3_bucket_tuple.count("bucket2"))

s3_bucket_tuple.index("bucket3") # this will give the index of "bucket3" in the tuple
print("Index of bucket3 in the tuple:", s3_bucket_tuple.index("bucket3"))

s3_bucket_tuple.append("bucket4") # this will give an error because tuples are immutable
print(s3_bucket_tuple)

s3_bucket_tuple.remove("bucket2") # this will give an error because tuples are immutable    
print(s3_bucket_tuple)