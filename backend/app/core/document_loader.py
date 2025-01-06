from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class DocumentLoader:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=20
        )

    def load_documents(self):
        loader = DirectoryLoader(
            self.data_path,
            glob='*.pdf',
            loader_cls=PyPDFLoader
        )
        return loader.load()

    def split_documents(self, documents):
        return self.text_splitter.split_documents(documents)