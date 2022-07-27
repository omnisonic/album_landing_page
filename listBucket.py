#this will list contents of the specified bucket.


import boto3
s3 = boto3.resource('s3')

my_bucket = s3.Bucket('johnclarkemusic')
for file in my_bucket.objects.all():
    print(file.key)
