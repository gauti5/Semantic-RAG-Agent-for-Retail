from langchain_core.prompts import ChatPromptTemplate

prompt=ChatPromptTemplate.from_template(
    """"
    you are a Retail Operation Specialist.
    Answer only from the provided context. Be Precise and Accurate.
    If the answer is not available, reply: 
    "I Couldn't find that information in the manual.
    chat history:
    {chat_history}
    context: 
    {context}
    question: 
    {question}
    answer:
    """
)