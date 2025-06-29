# 📄 LangChain PDF Chatbot

This is an intelligent chatbot application built using **LangChain**, **Flask**, **Pinecone** and **OpenAI**, capable of answering natural language questions based on the content of uploaded PDF documents.

### 🔍 Features

- **Retrieval-Augmented Generation (RAG)**: Uses semantic search with LangChain and Pinecone to retrieve relevant chunks from the PDF.
- **Persistent Conversation History**: Stores multi-turn chat conversations in an **SQLite** database using a custom memory class.
- **Streaming Support**: Implements token-level streaming with a custom handler to display responses in real-time.
- **Self-Learning Feedback Loop**: Integrated with **Langfuse** to track user feedback and dynamically weigh different chat models, memory strategies, and retrievers.
- **Task Queuing**: Uses a background worker and **Redis** to handle long-running embedding or processing tasks asynchronously.

---


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
