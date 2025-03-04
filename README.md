# AI-Powered Construction Task Manager

This project is a FastAPI-based microservice that simulates an AI-powered construction task manager. It utilizes the Gemini Pro API to generate task lists for construction projects and stores project data in an SQLite database.

## Features

-   **Project Creation:** Create new construction project requests via a POST API endpoint.
-   **Task Generation:** Uses the Gemini Pro API to dynamically generate task lists based on project details.
-   **Project Retrieval:** Retrieve project details, including tasks and status, via a GET API endpoint.
-   **Database Storage:** Stores project and task data in an SQLite database using SQLAlchemy.
-   **Background Task Simulation:** Simulates task completion using asyncio.
-   **Lifespan Event Handling:** Uses FastAPI's lifespan event handlers for application startup.

## Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/mohirbeck/construction_ai.git
    cd construction_ai
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
    .venv\Scripts\activate      # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**

    Create a `.env` file in the root directory of the project and add your Gemini Pro API key:

    ```
    GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
    ```

    Replace `YOUR_GEMINI_API_KEY` with your actual API key.

5.  **Run the application:**

    ```bash
    uvicorn app.main:app --reload
    ```

    The API will be available at `http://127.0.0.1:8000`.

## API Usage

### Create a Project (POST /projects/)

```bash
curl -X POST \
  http://127.0.0.1:8000/projects/ \
  -H 'Content-Type: application/json' \
  -d '{
    "project_name": "Restaurant",
    "location": "San Francisco"
  }'
```

### Retrieve project details

```bash
curl http://127.0.0.1:8000/projects/1
```