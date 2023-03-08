from google.cloud import bigquery

dataset_id = "{}.<데이터셋명>".format(client.project)

dataset = bigquery.Dataset(dataset_id)

dataset.location = "US"

dataset = client.create_dataset(dataset, timeout=30)
print("Created dataset {}.{}".format(client.project, dataset.dataset_id))
