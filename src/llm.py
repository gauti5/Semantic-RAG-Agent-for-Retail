
from src.retrieval import Retriever
from src.memory import memory
from src.prompt import prompt
from langchain_aws import ChatBedrock
from langchain_core.output_parsers import StrOutputParser
import boto3
from boto3.session import Session
import os
from dotenv import load_dotenv
load_dotenv()

AWS_REGION='us-east-1'
BEDROCK_MODEL=os.getenv('BEDROCK_MODEL_ID')

class RetailAssistant:
    def __init__(self, retriever):
        self.retriever=retriever
        session = boto3.session.Session(region_name=AWS_REGION)
        bedrock_runtime_client=session.client('bedrock-runtime',region_name=AWS_REGION)
        self.llm=ChatBedrock(
            client=bedrock_runtime_client, model_id=BEDROCK_MODEL, temperature=0
        )
        self.chain=(
            prompt
            | self.llm
            | StrOutputParser()
        )
        
    def ask(self, question):
        history=memory.load_memory_variables({})
        chat_history=history.get(
            "chat_history",
            []
        )
        docs=self.retriever.search(question)
        context="\n\n".join(doc.page_content for doc in docs)
        
        answer=self.chain.invoke(
            {
                "chat_history": chat_history,
                "context": context,
                "question": question
                
            }
        )
        memory.save_context(
            {"question": question},
            {"answer": answer}
      
        )

        return {
            
            "answer": answer,
            "documents": docs
        }





        
        
        '''pages = set()
        for doc in docs:
            pages.add(doc.metadata.get("page", "N/A"))

        for page in sorted(pages):
            print(f"Source Page: {page}")
        
            

        return answer'''


        