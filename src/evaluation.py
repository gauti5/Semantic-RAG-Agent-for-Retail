import sys
import types

# Must patch before any ragas import — ragas internally imports this removed module
_dummy = types.ModuleType("langchain_community.chat_models.vertexai")
_dummy.ChatVertexAI = None
sys.modules["langchain_community.chat_models.vertexai"] = _dummy

import os
import certifi
os.environ["AWS_CA_BUNDLE"] = certifi.where()

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from ragas.evaluation import evaluate
from ragas.llms.base import LangchainLLMWrapper
from ragas.embeddings.base import LangchainEmbeddingsWrapper
from langchain_aws import ChatBedrock, BedrockEmbeddings
import boto3
from dotenv import load_dotenv
load_dotenv()

from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall
)

from datasets import Dataset

data={
    'question': ["What is the required temperature range for the cold vault?"],
    'answer': ["The required temperature range for the cold vault is 34-38°F (1-3°C)."],
    'contexts': [['The cold vault (refrigerated beverage section) must maintain a temperature range of 34-38°F (1-3°C). All products must be front-faced with labels visible. The cold vault is restocked using the FIFO (First In, First Out) rotation method. Maximum door opening time for restocking is 10 minutes per section to maintain temperature compliance. Condensation on doors must be addressed immediately — report to maintenance if anti-fog heaters malfunction']],
    'reference': ['''The  cold  vault  (refrigerated  beverage  section)  must  maintain  a  temperature  range  of  34-38°F  (1-3°C).  All
products must be front-faced with labels visible. The cold vault is restocked using the FIFO (First In, First Out)
rotation method. Maximum door opening time for restocking is 10 minutes per section to maintain temperature
compliance.  Condensation  on  doors  must  be  addressed  immediately  —  report  to  maintenance  if  anti-fog
heaters malfunction''']
}
dataset=Dataset.from_dict(data)

bedrock_runtime = boto3.session.Session(region_name='us-east-1').client('bedrock-runtime', region_name='us-east-1')

llm = LangchainLLMWrapper(ChatBedrock(
    client=bedrock_runtime,
    model_id=os.getenv('BEDROCK_MODEL_ID'),
    temperature=0
))

embeddings = LangchainEmbeddingsWrapper(BedrockEmbeddings(
    client=bedrock_runtime,
    model_id=os.getenv('BEDROCK_EMBEDDING_MODEL')
))

faithfulness.llm = llm
answer_relevancy.llm = llm
answer_relevancy.embeddings = embeddings
context_precision.llm = llm
context_recall.llm = llm

result=evaluate(
    dataset,
    metrics=[
        faithfulness,
        answer_relevancy,
        context_recall,
        context_precision
    ]
)
print(result)
