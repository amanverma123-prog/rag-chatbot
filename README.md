# RAG Chatbot using Endee Vector Database

A Retrieval Augmented Generation (RAG) chatbot built with Endee vector database and Google Gemini AI.

## What is RAG?
RAG (Retrieval Augmented Generation) combines vector search with AI generation. Instead of relying purely on an LLM's training data, it first retrieves relevant context from a knowledge base, then generates accurate answers based on that context.

## Tech Stack
- **Endee** — High-performance vector database for storing and searching embeddings
- **Google Gemini** — For generating embeddings and AI responses
- **Python** — Core programming language

## Project Structure
rag-chatbot/
├── knowledge_base.txt   # Source knowledge for the chatbot
├── ingest.py            # Ingests knowledge base into Endee
├── chat.py              # Interactive RAG chatbot
├── .env                 # API keys (not pushed to GitHub)
└── README.md            # Project documentation

## How It Works
1. **Ingest** — Text from `knowledge_base.txt` is converted to vector embeddings using Gemini and stored in Endee
2. **Query** — User question is converted to a vector embedding
3. **Retrieve** — Endee finds the most semantically similar vectors
4. **Generate** — Gemini generates an answer using the retrieved context

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot
```

### 2. Install dependencies
```bash
pip install endee google-genai python-dotenv
```

### 3. Set up environment variables
Create a `.env` file in the root directory:
GEMINI_API_KEY=your_gemini_api_key
ENDEE_AUTH_TOKEN=your_endee_auth_token

### 4. Ingest the knowledge base
```bash
python ingest.py
```

### 5. Start chatting
```bash
python chat.py
```

## Demo
RAG Chatbot is ready! Type 'exit' to quit.
You: what is rag
Bot: RAG stands for Retrieval Augmented Generation, which combines search with AI generation.
You: what is a vector database
Bot: A vector database stores data as high-dimensional vectors for similarity search.
You: capital of india
Bot: The provided context does not contain information about the capital of India.

## Key Features
- Semantic search using vector embeddings
- Context-aware answers from knowledge base
- Gracefully handles out-of-scope questions
- Easy to extend with custom knowledge base

## Author
Aman Verma — [GitHub](https://github.com/amanverma123-prog) | [LinkedIn](https://linkedin.com/in/aman-verma-179062334)