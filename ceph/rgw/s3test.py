#!/usr/bin/python  
# -*- coding:utf-8 -*-  
import boto.s3.connection  
   
access_key = '1MWH3LWM1BS4ZF4HN5IH'     
secret_key ='cuObxYgtl1lJgqNxOIpENycVqXfxLxZ8z5IXDM0O'  
conn = boto.connect_s3(  
    aws_access_key_id=access_key,  
    aws_secret_access_key=secret_key,  
    host='{hostname}',port={port},  
    is_secure=False,calling_format=boto.s3.connection.OrdinaryCallingFormat(),  
)  
   
bucket = conn.create_bucket('my-new-bucket')  
for bucket in conn.get_all_buckets():  
    print"{name} {created}".format(  
        name=bucket.name,  
        created=bucket.creation_date,  
    )
