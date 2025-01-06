# Medical Chatbot Backend

A FastAPI-based backend for a medical chatbot that uses LangChain and Pinecone for processing and retrieving medical information from "The GALE ENCYCLOPEDIA of MEDICINE".

## Features

- FastAPI REST API
- LangChain for document processing and QA chain
- Pinecone vector store for efficient document retrieval
- PDF document loading and processing
- Modular and OOP-based architecture

## Project Structure

```
Medical-Chatbot-GenAI/
│   .gitignore
│   LICENSE
│   README.md
│
└───backend/
    │   .env
    │   requirements.txt
    │
    ├───app/
    │   │   main.py
    │   │
    │   ├───api/
    │   │   └───endpoints/
    │   │           chat.py
    │   │
    │   ├───config/
    │   │       settings.py
    │   │
    │   ├───core/
    │   │       document_loader.py
    │   │       embeddings.py
    │   │       llm.py
    │   │       pinecone_store.py
    │   │
    │   ├───models/
    │   │       schemas.py
    │   │
    │   └───services/
    │           chatbot.py
    │
    ├───data/
    │       medical_book.pdf
    │
    ├───model/
    │       llama-2-7b-chat.ggmlv3.q4_0.bin
    │
    └───research/
            trials.ipynb
```

## Prerequisites

- Python 3.8
- Pinecone API key
- The GALE ENCYCLOPEDIA of MEDICINE PDF document
- LLama model file (llama-2-7b-chat.ggmlv3.q4_0.bin)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd medical-chatbot/backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the backend directory with your Pinecone API key:
```
PINECONE_API_KEY=your-api-key-here
```

5. Place your medical encyclopedia PDF in the data directory:
```bash
mkdir data
# Copy your PDF file to the data directory
```

6. Place the LLama model file in the model directory:
```bash
mkdir model
# Copy llama-2-7b-chat.ggmlv3.q4_0.bin to the model directory
```

## Running the Application

1. Start the FastAPI server:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

2. Access the API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### POST /api/v1/chat

Send a medical question to the chatbot.

Request body:
```json
{
  "question": "What is diabetes?"
}
```

Response:
```json
{
  "answer": "Detailed answer about diabetes...",
  "sources": ["Relevant source passages from the encyclopedia..."]
}
```

## Configuration

Key configuration options in `app/config.py`:

```python
MODEL_PATH: str = "model/llama-2-7b-chat.ggmlv3.q4_0.bin"
MODEL_TYPE: str = "llama"
EMBEDDINGS_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
INDEX_NAME: str = "medibot"
DATA_PATH: str = "../data/"
```

## Development

### Adding New Features

1. Create new endpoints in `app/api/endpoints/`
2. Add new core functionality in `core/`
3. Create corresponding services in `services/`
4. Update models in `models/` if needed

