from google.cloud import bigquery
from google.oauth2 import service_account

KEY_PATH = "./config/key.json"
# Credentials 객체 생성
credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
# 구글 스토리지 클라이언트 객체 생성
client = bigquery.Client(credentials = credentials, project = credentials.project_id)

query_job = client.query(
    """
    SELECT
      CONCAT(
        'https://stackoverflow.com/questions/',
        CAST(id as STRING)) as url,
      view_count
    FROM `bigquery-public-data.stackoverflow.posts_questions`
    WHERE tags like '%google-bigquery%'
    ORDER BY view_count DESC
    LIMIT 10"""
)

results = query_job.result()  # Waits for job to complete.

for row in results:
    print("{} : {} views".format(row.url, row.view_count))
    
"""result
https://stackoverflow.com/questions/35159967 : 170023 views
https://stackoverflow.com/questions/22879669 : 142581 views
https://stackoverflow.com/questions/10604135 : 132406 views
https://stackoverflow.com/questions/44564887 : 128781 views
https://stackoverflow.com/questions/27060396 : 127008 views
https://stackoverflow.com/questions/12482637 : 120766 views
https://stackoverflow.com/questions/20673986 : 115720 views
https://stackoverflow.com/questions/39109817 : 108368 views
https://stackoverflow.com/questions/11057219 : 105175 views
https://stackoverflow.com/questions/43195143 : 101878 views
"""
