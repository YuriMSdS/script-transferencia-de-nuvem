import boto3
from google.cloud import storage

# Credenciais de acesso à AWS
aws_access_key_id = "SUA_CHAVE_DE_ACESSO"
aws_secret_access_key = "SUA_CHAVE_SECRETA"

# Credenciais de acesso ao GCP
gcp_credentials = '/path/to/credentials.json'

# Inicialização do S3

s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Inicialização do cliente GCP
storage_client = storage.Client.from_service_account_json(gcp_credentials)

# Nome do bucket S3 de origem
s3_bucket_name = 'nome-do-bucket-s3'

# Nome do bucket GCP de destino
gcp_bucket_name = 'nome-do-bucket-gcp'

# Lista de arquivos no bucket S3
s3_objects = s3.list_objects(Bucket=s3_bucket_name)['Contents']

# Copia cada arquivo do S3 para o GCP

for obj in s3_objects:
    file_data = s3.get_object(Bucket=s3_bucket_name, key=obj['Key'])

storage_client.bucket(gcp_bucket_name).blob(obj['Key']).upload_from_file(file_data['Body'])

print("Migração concluída")