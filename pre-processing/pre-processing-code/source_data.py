import urllib.request
import os
import boto3


def source_dataset(new_filename, s3_bucket, new_s3_key):

	source_dataset_url = 'https://opendata.arcgis.com/datasets/6ac5e325468c4cb9b905f1728d6fbf0f_0'

	# Download the file from `url` and save it locally under `file_name`:
	urllib.request.urlretrieve(
		source_dataset_url + '.geojson', '/tmp/' + new_filename + '.geojson')

	urllib.request.urlretrieve(
		source_dataset_url + '.csv', '/tmp/' + new_filename + '.csv')

	s3 = boto3.client('s3')
	asset_list = []

	for filename in os.listdir('/tmp'):
		print(filename)
		s3.upload_file('/tmp/' + filename, s3_bucket, new_s3_key + filename)
		asset_list.append({'Bucket': s3_bucket, 'Key': new_s3_key + filename})

	return asset_list
