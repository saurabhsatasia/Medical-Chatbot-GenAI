# Medical Chatbot

A full-stack medical chatbot application that uses FastAPI, React, and LangChain to provide medical information from "The GALE ENCYCLOPEDIA of MEDICINE".

![Medical Chatbot Screenshot](./screenshot.png)

## Features

### Backend
- FastAPI REST API
- LangChain for document processing and QA chain
- Pinecone vector store for efficient document retrieval
- PDF document loading and processing
- Modular and OOP-based architecture

### Frontend
- Modern React.js with Vite
- Elegant UI with shadcn/ui components
- Dark/Light theme support
- Real-time chat interface
- Source attribution for responses
- Responsive design

## Project Structure

```
Medical-Chatbot-GenAI/
├── README.md
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ui/            # shadcn components
│   │   │   ├── ChatInput.jsx
│   │   │   ├── ChatMessage.jsx
│   │   │   ├── ChatWindow.jsx
│   │   │   ├── ThemeToggle.jsx
│   │   │   └── theme-provider.jsx
│   │   ├── lib/
│   │   │   └── api.js
│   │   └── App.jsx
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
│
└── backend/
    ├── app/
    │   ├── main.py
    │   ├── api/
    │   │   └── endpoints/
    │   │       └── chat.py
    │   ├── config/
    │   │   └── settings.py
    │   ├── core/
    │   │   ├── document_loader.py
    │   │   ├── embeddings.py
    │   │   ├── llm.py
    │   │   └── pinecone_store.py
    │   ├── models/
    │   │   └── schemas.py
    │   └── services/
    │       └── chatbot.py
    ├── data/
    │   └── medical_book.pdf
    ├── model/
    │   └── llama-2-7b-chat.ggmlv3.q4_0.bin
    └── requirements.txt

```

## Prerequisites

- Python 3.8
- Node.js 16+ and npm
- Pinecone API key
- The GALE ENCYCLOPEDIA of MEDICINE PDF document
- LLama model file (llama-2-7b-chat.ggmlv3.q4_0.bin)

## Installation

### Backend Setup

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

4. Create a `.env` file in the backend directory:
```
PINECONE_API_KEY=your-api-key-here
```

5. Set up data and model:
```bash
mkdir data model
# Copy medical_book.pdf to data directory
# Copy llama-2-7b-chat.ggmlv3.q4_0.bin to model directory
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd ../frontend
```

2. Install dependencies:
```bash
npm install
```

3. Update the API URL in `src/lib/api.js` if needed:
```javascript
const API_BASE_URL = 'http://localhost:8000/api/v1';
```

## Running the Application

1. Start the backend server:
```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

2. Start the frontend development server:
```bash
cd frontend
npm run dev
```

3. Access the application:
- Frontend: http://localhost:5173
- API Documentation: http://localhost:8000/docs

## API Endpoints

### POST /api/v1/chat

Send a medical question to the chatbot.

Request:
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

### Backend Configuration
Key settings in `app/config/settings.py`:
```python
MODEL_PATH: str = "model/llama-2-7b-chat.ggmlv3.q4_0.bin"
MODEL_TYPE: str = "llama"
EMBEDDINGS_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
INDEX_NAME: str = "medibot"
DATA_PATH: str = "../data/"
```

### Frontend Configuration
Theme configuration in `src/index.css`:
```css
:root {
  /* Light theme variables */
}

.dark {
  /* Dark theme variables */
}
```

## Features Showcase

### Chat Interface
- Real-time message updates
- User messages appear on the right (blue)
- Bot responses appear on the left with sources
- Loading indicators for responses
- Smooth scrolling chat history

### Theme Support
- Light/Dark mode toggle
- Persistent theme preference
- Smooth theme transitions

### Responsive Design
- Mobile-friendly interface
- Adaptive layout
- Accessible on all screen sizes

## Development

### Adding New Features

#### Backend
1. Create new endpoints in `app/api/endpoints/`
2. Add core functionality in `core/`
3. Create services in `services/`
4. Update models in `models/`

#### Frontend
1. Add new components in `src/components/`
2. Update API client in `src/api.js`
3. Modify theme in `src/index.css`
4. Add new pages in `src/pages/`
