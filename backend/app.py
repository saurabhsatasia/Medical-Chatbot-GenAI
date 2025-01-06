import os
from dotenv import load_dotenv

from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

from langchain_pinecone import PineconeVectorStore
from langchain import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA






load_dotenv()

PINECON_API_KEY = os.getenv("PINECON_API_KEY")
os.environ['PINECONE_API_KEY'] = PINECON_API_KEY

# Extract the data from the PDF
def load_pdf(data_path):
    loader = DirectoryLoader(data_path, glob='*.pdf', loader_cls=PyPDFLoader)
    return loader.load()

# Split the extracted data into text chunks
def split_text(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks

# Download the embeddings model from Hugging Face
def download_embeddings_model(model_name='sentence-transformers/all-MiniLM-L6-v2'):
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    return embeddings

# def download_embeddings_model(model_name='sentence-transformers/all-MiniLM-L6-v2'):
#     model = SentenceTransformer(model_name)
#     return model

extracted_data = load_pdf(data_path='../data/')
print(f'Length of extracted data {len(extracted_data)}')

text_chunks = split_text(extracted_data)
print(f'Length of text chunks {len(text_chunks)}')

embeddings = download_embeddings_model(model_name='sentence-transformers/all-MiniLM-L6-v2')  # 384
embed_dimension = embeddings.get_sentence_embedding_dimension()
print(f"The embedding dimension for the model is {embed_dimension}.")

index_name = "medibot"
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings,
)

# Load exsiting pincone index
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings,)

prompt_template="""
Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs={"prompt": PROMPT}

llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                  model_type="llama",
                  config={'max_new_tokens':512,
                          'temperature':0.8})


qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
        return_source_documents=True,
        chain_type_kwargs=chain_type_kwargs
        )


