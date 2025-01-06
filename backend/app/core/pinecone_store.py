from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from app.config.settings import settings


class VectorStoreManager:
    def __init__(self, index_name: str, embeddings):
        self.index_name = index_name
        self.embeddings = embeddings
        self.store = None
        self.pc = Pinecone(
            api_key=settings.PINECONE_API_KEY
        )
        self._ensure_index_exists()

    def create_store(self, documents):
        self.store = PineconeVectorStore.from_documents(
            documents=documents,
            index_name=self.index_name,
            embedding=self.embeddings
        )
        return self.store

    def _ensure_index_exists(self):
        """Ensure the Pinecone index exists, create if it doesn't"""
        existing_indexes = [index.name for index in self.pc.list_indexes()]

        if self.index_name not in existing_indexes:
            # Create index
            self.pc.create_index(
                name=self.index_name,
                dimension=384,  # dimension for 'all-MiniLM-L6-v2'
                metric='cosine',
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-east-1"
                )
            )

    def load_existing_store(self):
        """Load existing Pinecone index"""
        self.store = PineconeVectorStore.from_existing_index(
            index_name=self.index_name,
            embedding=self.embeddings
        )
        return self.store