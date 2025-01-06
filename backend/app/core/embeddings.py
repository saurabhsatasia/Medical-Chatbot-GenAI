from langchain_community.embeddings import HuggingFaceEmbeddings
#TODO run `pip install -U langchain-huggingface` and import as `from langchain_huggingface import HuggingFaceEmbeddings`
class EmbeddingsManager:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.embeddings = None

    def load_embeddings(self):
        self.embeddings = HuggingFaceEmbeddings(model_name=self.model_name)
        return self.embeddings

    def get_embedding_dimension(self):
        if not self.embeddings:
            self.load_embeddings()
        return self.embeddings.get_sentence_embedding_dimension()