from google.cloud import storage
from google.cloud import bigquery

def gcs2bq(event, context):
    client = bigquery.Client()

    dataset_id = 'your_dataset'
    bucket_name = event['bucket']
    file_name = event['name']
    
    table_id = file_name.split('.')[0]
    file_ext = file_name.split('.')[-1]

    if file_ext == 'csv':
        uri = 'gs://' + bucket_name + '/' + file_name
        dataset_ref = client.dataset(dataset_id)
        table_ref = dataset_ref.table(table_id)

        job_config = bigquery.LoadJobConfig()
        job_config.autodetect = True
        job_config.schema_update_options = [
            bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION
        ]
        job_config.create_disposition = [
            bigquery.CreateDisposition.CREATE_IF_NEEDED
        ]

        load_job = client.load_table_from_uri(
            uri, table_ref, job_config=job_config
        )
        
        load_job.result()
        destination_table = client.get_table(dataset_ref.table(table_id))

    else:
        print('Not CSV File')
        
""" requirements.txt
# Function dependencies, for example:
# package>=version
google.cloud.bigquery
google.cloud.storage
"""
