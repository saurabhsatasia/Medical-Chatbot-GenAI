from app.core.document_loader import DocumentLoader
from app.core.embeddings import EmbeddingsManager
from app.core.pinecone_store import VectorStoreManager
from app.core.llm import LLMManager
from app.config.settings import settings


class ChatbotService:
    def __init__(self):
        self.document_loader = DocumentLoader(settings.DATA_PATH)
        self.embeddings_manager = EmbeddingsManager(settings.EMBEDDINGS_MODEL)
        self.embeddings = self.embeddings_manager.load_embeddings()
        self.vector_store = VectorStoreManager(settings.INDEX_NAME, self.embeddings)
        self.llm_manager = LLMManager(settings.MODEL_PATH, settings.MODEL_TYPE)
        self.initialize_service()

    def initialize_service(self):
        # Load and process documents
        documents = self.document_loader.load_documents()
        text_chunks = self.document_loader.split_documents(documents)

        # Initialize vector store
        try:
            self.vector_store.load_existing_store()
        except:
            self.vector_store.create_store(text_chunks)

        # Initialize LLM and QA chain
        prompt_template = """
        Use the following pieces of information to answer the user's question.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.
        
        Guidelines:
        - Provide a clear, concise answer
        - Avoid repeating words or phrases
        - Use natural, flowing language
        - Stay focused on the question
        - If the source text contains repetitions, summarize it clearly

        Context: {context}
        Question: {question}

        Only return the helpful answer below and nothing else.
        Helpful answer (be concise and avoid repetitions):
        """

        self.qa_chain = self.llm_manager.create_qa_chain(
            self.vector_store.store.as_retriever(search_kwargs={'k': 2}),
            prompt_template
        )

    async def get_response(self, question: str):
        response = self.qa_chain(question)
        return {
            "answer": response["result"],
            "sources": [doc.page_content for doc in response["source_documents"]]
        }