import os
import pandas as pd
import boto3

source_data = 'https://opendata.arcgis.com/datasets/6ac5e325468c4cb9b905f1728d6fbf0f_0.csv'


def source_dataset(s3_bucket, new_s3_key):

    df = pd.read_csv(source_data, index_col=None)

    df.columns = df.columns.str.lower()
    df = df.applymap(lambda s: s.lower() if type(s) == str else s)

    df.to_csv('/tmp/hospitals.csv', index=False)

    s3 = boto3.client('s3')
    s3.upload_file('/tmp/hospitals.csv', s3_bucket, new_s3_key)
