from google import genai
from endee import Endee
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ENDEE_AUTH_TOKEN = os.getenv("ENDEE_AUTH_TOKEN")

# Initialize clients
gemini = genai.Client(api_key=GEMINI_API_KEY)
endee = Endee(ENDEE_AUTH_TOKEN)

# Get index
index = endee.get_index(name="rag_index")

def search_context(query):
    result = gemini.models.embed_content(
        model="gemini-embedding-001",
        contents=query,
        config={"output_dimensionality": 768}
    )
    query_vector = result.embeddings[0].values
    results = index.query(vector=list(query_vector), top_k=3)
    context = "\n".join([r["meta"]["text"] for r in results])
    return context

def chat(question):
    context = search_context(question)
    prompt = f"""You are a helpful AI assistant. Use the context below to answer the question.
    
Context:
{context}

Question: {question}

Answer:"""
    response = gemini.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

# Main chat loop
print("RAG Chatbot is ready! Type 'exit' to quit.\n")
while True:
    question = input("You: ")
    if question.lower() == "exit":
        break
    answer = chat(question)
    print(f"\nBot: {answer}\n")