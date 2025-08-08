# 📄 LangChain PDF Chatbot

This is an intelligent chatbot application built using **LangChain**, **Flask**, **Pinecone** and **OpenAI**, capable of answering natural language questions based on the content of uploaded PDF documents.

### 🚀 Features

### **1. Document Ingestion & Vector Storage**
- **PDF Parsing** using `PyPDFLoader` for text extraction from PDF files.
- **Pinecone Vector Store** integration for persistent, high-speed similarity search.
- **Metadata-Enhanced Indexing** to scope retrievals and improve relevance.

### **2. Multi-Model LLM Integration**
- Uses **OpenAI GPT-4o** and **GPT-3.5 Turbo** for different stages of the pipeline.
- Implements an **LLM Map** to dynamically select the appropriate model for streaming or non-streaming tasks.

### **3. Custom Retrieval Pipeline**
- **Custom Retriever** built for Pinecone to control query behavior and scoring.
- **Component Scoring System** with feedback-driven selection — retrieves past component usage for a conversation and reuses it, or selects a new one based on scoring logic.
- **Retriever Maps** to compare different retrievers and learn from user feedback on the most effective one.
- **Generalized Component Picker** to support varied retrieval strategies.

### **4. Advanced Conversational Memory**
- **SQL Buffer Memory Map** for persistent conversation state storage.
- **Custom `MsgHistory` Class** to manage conversation history.
- **Windowed Memory Map (k=5)** to maintain only the most recent interactions for concise, relevant prompts.
- **Memory Mapping** for multi-session support.

### **5. Real-Time Streaming Responses**
- **Custom Streaming Handler** for token-by-token model output delivery.
- Support for **session-specific queues** to isolate concurrent conversations.
- Optional **non-streaming mode** for synchronous operations.

### **6. RAG Architecture**
- **Retriever-Augmented Generation** pipeline that blends:
  - Vector store retrieval
  - Contextual prompt construction
  - LLM-powered completion
- Tuned **Condense Question Chain** to reframe follow-up questions using non-streaming models for efficiency.


### **7. Job Processing & Scalability**
- **Redis-backed Job Queue** to handle background tasks efficiently.
- Worker process architecture for async document ingestion and indexing.

### **8. Robust Session & Context Management**
- **Unique Session Queues** to isolate user streams.
- **Scoped Retrieval** to ensure only relevant documents per session are accessed.

---
### 🛠️ Tech Stack
- **Backend:** Python, LangChain  
- **Vector DB:** Pinecone  
- **Queue & Cache:** Redis  
- **Document Loader:** PyPDFLoader  
- **LLMs:** OpenAI GPT-4o, GPT-3.5 Turbo  
- **Memory & Retrieval:** Custom LangChain Components, SQL Buffer Memory, Window Memory  
- **Monitoring:** LangFuse  

# ⚙️ Environment Setup

Before running the application, create a `.env` file in the project root and define the following environment variables:

```shell
# OpenAI
OPENAI_API_KEY=your_openai_api_key

# Pinecone
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_env_name   # e.g., us-east-1 (AWS)
PINECONE_HOST=your_pinecone_host_url
PINECONE_INDEX_NAME=your_index_name

# Langfuse
LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
LANGFUSE_SECRET_KEY=your_langfuse_secret_key

# Redis
REDIS_URL=redis://localhost:6379 OR Cloud URI 
```
# 🚀 First Time Setup

## Using Pipenv [Recommended]

```bash
# Install dependencies
pipenv install

# Create a virtual environment
pipenv shell

# Initialize the database
flask --app app.web init-db
```


# Running the app [Pipenv]

There are three separate processes that need to be running for the app to work: the server, the worker, and Redis.

If you stop any of these processes, you will need to start them back up!

Commands to start each are listed below. If you need to stop them, select the terminal window the process is running in and press Control-C

### To run the Python server

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

Then:

```
inv dev
```

### To run the worker

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

Then:

```
inv devworker
```

### To run Redis

```
redis-server
```

### To reset the database

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

Then:
```
flask --app app.web init-db
```

---

## 🧠 How It Works
```
Once set up, the server will start at `http://127.0.0.1:8000`.

1. **Sign up or log in** to begin a session.
2. **Set up Pinecone** and **start your Redis server** before uploading any documents.
3. **Upload a PDF** through the interface.
4. You can then start chatting with the chatbot — it understands and extracts information from the document to answer your questions.
5. A **toggle switch** lets you turn **streaming** on or off for real-time token-by-token responses.
6. Use the **"New Chat"** feature to start multiple conversations on the same uploaded PDF.
7. All chats, messages, and session data are **persisted in the SQLite database** for long-term storage and retrieval.
```
---
