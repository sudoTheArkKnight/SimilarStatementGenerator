from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load the pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

class UserInput(BaseModel):
    statement: str

@app.post("/similar_statements/")
async def get_similar_statements(user_input: UserInput):
    # Convert the input statement to a vector
    input_embedding = model.encode([user_input.statement])

    # Example dataset of statements
    statements = [
        "Hello World",
        "How are you?",
        "Good morning",
        "Good night",
        "Have a nice day",
        "See you later",
        "Take care",
        "What's your name?",
        "Where are you from?",
        "What do you do?"
    ]

    # Precompute the embeddings for the example statements
    statement_embeddings = model.encode(statements)

    # Compute cosine similarities
    similarities = cosine_similarity(input_embedding, statement_embeddings)

    # Get the indices of the top 10 most similar statements
    top_indices = np.argsort(similarities[0])[::-1][:10]

    # Retrieve the most similar statements
    similar_statements = [statements[i] for i in top_indices]

    return {"similar_statements": similar_statements}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)