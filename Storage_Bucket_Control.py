from google.cloud import storage
from google.oauth2 import service_account

# 서비스 계정 인증 정보가 담긴 JSON 파일 경로
KEY_PATH = "./config/key.json"
# Credentials 객체 생성
credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
# 구글 스토리지 클라이언트 객체 생성
client = storage.Client(credentials = credentials, project = credentials.project_id)

"""
파일 업로드
"""

bucket_name = "<Bucket 명>"
blob_name = "<Blob 명>"
file_path = "<적재할 파일 경로>"

bucket = client.get_bucket(bucket_name)
blob = bucket.blob(blob_name)
blob.upload_from_filename(file_path)

# 버킷에 업로드된 객체의 공개 URL
print(blob.public_url)

"""
파일 삭제
"""

bucket = client.bucket(bucket_name)
blob = bucket.blob(blob_name)
blob.delete()
