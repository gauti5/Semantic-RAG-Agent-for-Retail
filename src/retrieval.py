
class Retriever:
    def __init__(self, db):
        self.retriever=db.as_retriever(
            search_type='mmr',
            search_kwargs={'k':1}
        )
    def search(self, question):
        retrieved_docs=self.retriever.invoke(question)

        return retrieved_docs
        