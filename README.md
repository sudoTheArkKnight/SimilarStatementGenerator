# Similar Statement Generator

This project is a web application that finds similar statements to a given input statement using FastAPI and a pre-trained SentenceTransformer model.

## Features

- Accepts a user input statement via a web form.
- Uses a pre-trained SentenceTransformer model to find similar statements.
- Displays the top 10 most similar statements.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- SentenceTransformer
- scikit-learn
- numpy

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/sudoTheArkKnight/SimilarStatementGenerator.git
    cd SimilarStatementGenerator
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the FastAPI server:
    ```sh
    uvicorn main:app --host 127.0.0.1 --port 8000
    ```

2. Open your web browser and navigate to:
    ```
    http://127.0.0.1:8000/static/index.html
    ```

## Project Structure

- `main.py`: The main FastAPI application file.
- `static/index.html`: The HTML file for the web interface.
- `requirements.txt`: The list of required Python packages.
- `.gitignore`: Git ignore file to exclude certain files and directories.

## API Endpoints

- `POST /similar_statements/`: Accepts a JSON payload with a `statement` field and returns the top 10 most similar statements.

## Example

To test the API, you can use the following HTTP request:

```http
POST http://127.0.0.1:8000/similar_statements/
Content-Type: application/json

{
  "statement": "Good evening"
}
