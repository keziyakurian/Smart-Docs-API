# How to Run: Smart Docs Q&A API

This guide will help you set up and run the AI-powered Smart Docs API locally.

## Prerequisites
- Python 3.10+
- OpenAI API Key (You need credits)

## Setup

1.  **Clone/Navigate** to the project folder:
    ```bash
    cd smart-docs-api
    ```

2.  **Create Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment**:
    - Open `.env`
    - Replace `sk-proj-YOUR_KEY_HERE` with your actual OpenAI API Key.

## Running the App

Run the server using Uvicorn:
```bash
uvicorn app.main:app --reload
```

The API will be live at: `http://localhost:8000`

## Using the API (Swagger UI)

1.  Go to `http://localhost:8000/docs`.
2.  **Upload a PDF**:
    - Click `POST /api/v1/upload`.
    - Upload a sample PDF (e.g., a resume or manual).
    - Execute.
3.  **Ask a Question**:
    - Click `POST /api/v1/query`.
    - Enter a JSON body like:
      ```json
      {
        "question": "What is the main summary of this document?"
      }
      ```
    - Execute to see the AI's answer!
