import logging
import boto3
from botocore.exceptions import ClientError

bucket_name  ='jctech-log'

def get_bucket_cors(bucket_name):
    """Retrieve the CORS configuration rules of an Amazon S3 bucket

    :param bucket_name: string
    :return: List of the bucket's CORS configuration rules. If no CORS
    configuration exists, return empty list. If error, return None.
    """

    # Retrieve the CORS configuration
    s3 = boto3.client('s3')
    try:
        response = s3.get_bucket_cors(Bucket=bucket_name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchCORSConfiguration':
            return []
        else:
            # AllAccessDisabled error == bucket not found
            logging.error(e)
            return None
    return response['CORSRules']
    print(response['CORSRules'])

get_bucket_cors(bucket_name)
