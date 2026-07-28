from langchain_aws import ChatBedrock
from langchain_classic.agents import (
    AgentExecutor,
    create_tool_calling_agent
)
from langchain.tools import tool
from langchain_classic.memory import ConversationBufferWindowMemory
from langchain_core.prompts import ChatPromptTemplate
import boto3
import os

AWS_REGION = "us-east-1"
BEDROCK_MODEL = os.getenv("BEDROCK_MODEL_ID")


class RetailAgent:

    def __init__(self, retriever):

        session = boto3.session.Session(
            region_name=AWS_REGION
        )

        bedrock_runtime_client = session.client(
            "bedrock-runtime",
            region_name=AWS_REGION
        )

        self.llm = ChatBedrock(
            client=bedrock_runtime_client,
            model_id=BEDROCK_MODEL,
            temperature=0
        )

        self.memory = ConversationBufferWindowMemory(
            memory_key="chat_history",
            k=5,
            return_messages=True
        )

        self.retriever = retriever
        self.last_docs = []

        
        retriever_tool = tool(
            "RetailRetriever",
            self.search_manual,
            description="Retrieve retail documents"
        )


        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
                    
                    You are a Retail Operations Assistant.
                    Answer only from the provided context. Be Precise and Accurate.
                    Do not provide additional explanations unless explicitly requested.
                    If information is unavailable, respond:
                    'I couldn't find that information in the retail manual.'
                    """
                ),
                ("placeholder", "{chat_history}"),
                ("human", "{input}"),
                ("placeholder", "{agent_scratchpad}")
            ]
        )

        agent = create_tool_calling_agent(
            self.llm,
            [retriever_tool],
            prompt
        )

        self.agent_executor = AgentExecutor(
            agent=agent,
            tools=[retriever_tool],
            memory=self.memory,
            verbose=False
        )

    def search_manual(self, question):

        docs = self.retriever.search(question)

        self.last_docs = docs

        if not docs:
            return "No relevant information found in the retail manual."

        results = []

        for doc in docs:
            results.append(
                f"""
Page: {doc.metadata.get('page', 'N/A')}
Heading: {doc.metadata.get('heading', 'Unknown')}

{doc.page_content}
"""
            )

        return "\n\n".join(results)

    def ask(self, question):

        self.last_docs = self.retriever.search(question)

        response = self.agent_executor.invoke(
            {
                "input": question
            }
        )

        answer = response["output"]

        if isinstance(answer, list):
            answer = " ".join(
                item.get("text", "")
                for item in answer
                if isinstance(item, dict)
            )

        return {
            "answer": answer.strip(),
            "documents": self.last_docs
        }
