

from langchain_aws import BedrockEmbeddings
import boto3
from dotenv import load_dotenv
import os

load_dotenv()
embedding_model=os.getenv('BEDROCK_EMBEDDING_MODEL')
AWS_REGION= "us-east-1"

class EmbeddingService:
    def __init__(self):
        session = boto3.Session(region_name= AWS_REGION)
        bedrock_runtime_client = session.client('bedrock-runtime',region_name=AWS_REGION)
        
        self.embeddings=BedrockEmbeddings(client=bedrock_runtime_client,model_id=embedding_model)
    def get_embeddings(self):
        return self.embeddings