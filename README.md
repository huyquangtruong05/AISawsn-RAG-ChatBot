# 🤖 AISawsn – Local AI Chatbot with RAG

<p align="center">
  <img src="frontend/img/logo.png" width="250" alt="AISawsn Platform">
</p>

<p align="center">
  A local AI chatbot powered by <b>RAG (Retrieval Augmented Generation)</b>,  
  running fully offline with <b>TinyLlama + Ollama + FastAPI + SQLite</b>.
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-blue">
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-Backend-green">
  <img alt="FAISS" src="https://img.shields.io/badge/VectorDB-FAISS-orange">
  <img alt="SQLite" src="https://img.shields.io/badge/Database-SQLite-blue">
  <img alt="Ollama" src="https://img.shields.io/badge/LLM-Ollama-red">
</p>

---

## 📑 Table of Contents

- [About The Project](#-about-the-project)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [System Architecture](#-system-architecture)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [RAG Pipeline](#-rag-pipeline)
- [Future Improvements](#-future-improvements)
- [Contact](#-contact)

---

## 📖 About The Project

Large Language Models (LLMs) are incredibly powerful, but they have a major limitation: **they cannot access private, up-to-date, or domain-specific knowledge.**

This project solves that problem using **Retrieval Augmented Generation (RAG)**. AISawsn allows you to chat with your own documents securely and privately. 

The chatbot can:
- Read custom **PDF knowledge bases**.
- Convert text into **vector embeddings**.
- Retrieve highly relevant information using semantic search.
- Generate accurate, context-aware answers using a **local LLM**.
- Manage user data securely using **SQLite**.

Everything runs **100% locally** with **Ollama + TinyLlama**, meaning:
- 🔒 **Privacy First:** No data is ever sent to external APIs (like OpenAI).
- ⚡ **Fast Responses:** Optimized local inference.
- 🧠 **Custom Knowledge:** Tailor the AI to your specific documents.

---

## ✨ Key Features

- **✅ Local AI Chatbot:** Fully offline generation, no API keys required.
- **✅ RAG Pipeline:** Context-aware answers based on your documents.
- **✅ Document Ingestion:** Built-in PDF knowledge base support.
- **✅ FAISS Vector Database:** Fast and efficient similarity search.
- **✅ Advanced Retrieval:** Features semantic search and a reranker (Cross-Encoder) for superior document relevance.
- **✅ Ollama Integration:** Seamless local LLM management with TinyLlama.
- **✅ FastAPI Backend:** High-performance, async RESTful API.
- **✅ User Management:** SQLite database for handling user sessions and data.
- **✅ Frontend Interface:** Clean and responsive HTML/CSS/JS chat UI.

---

## 🧰 Tech Stack

### Languages
- Python 3.10+
- JavaScript, HTML, CSS

### AI & Machine Learning
- **LLM:** TinyLlama (via Ollama)
- **Embeddings & Reranking:** Sentence Transformers
- **Architecture:** Retrieval Augmented Generation (RAG)

### Backend & Database
- **Framework:** FastAPI, Uvicorn
- **Relational DB:** SQLite (User data & authentication)
- **Vector DB:** FAISS (Document embeddings)

### Data Processing
- **Parsing:** PyPDF
- **Pipeline:** Text Chunking + Vectorization

---

## 🏗 System Architecture

```text
User 
 │
 ▼
Frontend Chat UI
 │
 ▼
FastAPI Backend ───────────────► SQLite (User Auth & Data)
 │
 ▼
RAG Pipeline
 ├── 1. Embed user question
 ├── 2. Vector search (FAISS)
 ├── 3. Reranker (Cross Encoder)
 └── 4. Retrieve top documents
 │
 ▼
Prompt Construction (Context + Question)
 │
 ▼
TinyLlama (via Ollama)
 │
 ▼
Generated Answer
 │
 ▼
Return to User
```

## 📂 Project Structure
```text
ai_chatbot/
│
├── backend/
│   ├── app/
│   │   ├── rag/
│   │   │   ├── embedder.py
│   │   │   ├── vector_store.py
│   │   │   ├── reranker.py
│   │   │   ├── prompt.py
│   │   │   ├── llm.py
│   │   │   └── rag_pipeline.py
│   │   ├── auth.py
│   │   ├── config.py
│   │   ├── crud.py
│   │   ├── database.py       <-- SQLite connection setup
│   │   ├── main.py
│   │   ├── models.py         <-- SQLite schemas
│   │   └── schemas.py        <-- Pydantic models
│   │
│   ├── scripts/
│   │   └── build_vector_db.py
│   │
│   └── vector_db/            <-- Generated after running indexing script
│       ├── documents.pkl
│       ├── faiss.index
│       └── metadata.pkl
│
├── data/
│   └── pdf_files/            <-- Place your knowledge base PDFs here
│
├── frontend/
│   ├── css/
│   │   ├── landing.css
│   │   └── style.css
│   ├── img/
│   │   └── logo.png
│   ├── js/
│   │   ├── landing.js
│   │   └── style.js
│   ├── index.html
│   └── landing.html
│
├── models/
│   ├── data.json
│   ├── Modelfile
│   ├── prepare_model_ai.ipynb
│   └── tinyllama-chat.Q4_K_M.gguf
│
├── requirements.txt
└── README.md
```

## 🚀 Getting Started
### 1️⃣ Prerequisites

Ensure you have the following installed:

- **Python 3.10+** – [Download Python](https://www.python.org/downloads/)
- **Git** – [Download Git](https://git-scm.com/downloads)
- **Ollama** – [Download Here](https://ollama.com/download)

### 2️⃣ Troubleshooting Ollama (Windows)
If you install Ollama and get an error like 'ollama' is not recognized as an internal or external command, you need to add it to your System PATH:

- 1. Press Windows + S, search for Environment Variables, and select Edit the system environment variables.

- 2. Click the Environment Variables button.

- 3. Under System variables, find and select Path, then click Edit.

- 4. Click New and add the following path:
```
C:\Users\<Your-Username>\AppData\Local\Programs\Ollama (Replace <Your-Username> with your actual Windows username).
```
- 5. Restart your terminal or VS Code.

- 6. Verify the installation by running:
```
ollama --version
```

## 📦 Installation & Setup
### 1. Clone the repository
```
git clone https://github.com/huyquangtruong05/AISawsn-RAG-ChatBot.git
cd AISawsn-RAG-ChatBot
```

### 2. Create and activate a virtual environment
```
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Download the TinyLlama model
Open and run all cells in the Jupyter notebook **models/prepare_model_ai.ipynb**.
This will download the TinyLlama model file **tinyllama-chat.Q4_K_M.gguf**.
After the download completes, move the **.gguf** file into the **models/ folder (if not already there)**.

## 🤖 Setup Local LLM (TinyLlama)
Navigate to the models directory where your .gguf file is located and create/edit the Modelfile:
```
FROM ./tinyllama-chat.Q4_K_M.gguf

PARAMETER temperature 0.7
PARAMETER num_ctx 2048

SYSTEM You are a helpful AI assistant that answers questions using context.
```
Build the model in Ollama:
```
ollama create tinyllama-rag -f Modelfile
```
Verify the model was created successfully:
```
ollama list
# You should see 'tinyllama-rag' in the output

ollama run tinyllama-rag
# Ask a test question like "What is AI?" to ensure it is working.
```

## 🧠 Build Vector Database
- 1. Place your target PDF files into the data/pdf_files/ folder.
- 2. Run the indexing script from the project root:
     ```
     python backend/scripts/build_vector_db.py
     ```
    This will process your PDFs and generate faiss.index, documents.pkl, and metadata.pkl inside the backend/vector_db/ directory.
## ▶️ Run the Backend
Start the FastAPI server: 
```
uvicorn backend.app.main:app --reload
```
- Server URL: http://127.0.0.1:8000
- Interactive API Docs (Swagger): http://127.0.0.1:8000/docs
## 💬 Usage
You can test the API using tools like Postman, cURL, or through the frontend UI.
- Example API Request (cURL):
```
curl -X POST "[http://127.0.0.1:8000/chat](http://127.0.0.1:8000/chat)" \
     -H "Content-Type: application/json" \
     -d '{"question": "What is Retrieval Augmented Generation?"}'
```
- Example JSON Response:
```
{
  "answer": "Retrieval Augmented Generation (RAG) is a technique that enhances large language models by retrieving relevant data from a custom knowledge base before generating a response..."
}
``` 
(Note: If you have implemented SQLite authentication endpoints like /login or /register, you will need to authenticate before accessing the /chat endpoint).



## 🔎 RAG Pipeline Breakdown
- User Question: The user submits a query via the frontend.

- Text Embedding: The question is converted into vector format using Sentence Transformers.

- Vector Search (FAISS): The system quickly finds the top-K most mathematically similar text chunks in the database.

- Reranker: A Cross-Encoder evaluates the retrieved chunks and re-orders them based on actual semantic relevance to the question.

- Prompt Construction: The top documents are combined with the user's question into a strict prompt template.

- LLM Generation: TinyLlama (running locally via Ollama) reads the context and generates an informed answer.

## 🚀 Future Improvements
-  Implement streaming responses for real-time typing effect.

-  Add conversational memory (chat history tracking).

-  Support multi-document format retrieval (.docx, .txt, .csv).

- Integrate external web search fallback.

-  Enhance UI/UX for the frontend application.

-  Dockerize the entire application for one-click deployment.

-  Optimize inference for GPU acceleration.

## 📬 Contact
- Author: Truong Quang Huy

- GitHub: huyquangtruong05/AISawsn-RAG-ChatBot

- Email: huyquangtruong.programmer@gmail.com
