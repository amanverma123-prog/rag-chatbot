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

# Delete old index if exists
print("Deleting old index if exists...")
try:
    endee.delete_index(name="rag_index")
    print("Old index deleted!")
except Exception as e:
    print(f"No old index found: {e}")

# Create index with dimension 768
print("Creating index...")
endee.create_index(
    name="rag_index",
    dimension=768,
    space_type="cosine"
)
print("Index created!")

# Get index
index = endee.get_index(name="rag_index")

# Read knowledge base
with open("knowledge_base.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

# Generate embeddings and store in Endee
print("Ingesting data...")
for i, line in enumerate(lines):
    result = gemini.models.embed_content(
        model="gemini-embedding-001",
        contents=line,
        config={"output_dimensionality": 768}
    )
    embedding = result.embeddings[0].values
    index.upsert([{
        "id": str(i),
        "vector": list(embedding),
        "meta": {"text": line}
    }])
    print(f"Ingested: {line[:50]}...")

print("All data ingested successfully!")