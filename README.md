# FastAPI DateTime API

This is a simple FastAPI application that provides the current date and time in ISO 8601 format (UTC) based on the Africa/Lagos timezone.

## Features
- Accepts `GET` requests.
- Returns the current date and time dynamically.
- Responds with an appropriate HTTP status code.
- Well-structured and documented code.
- Deployed to a publicly accessible endpoint.

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python (>=3.7)
- pip
- Virtual environment (optional but recommended)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/omofz/stage0-hng.git
    cd stage0-hng
    ```

2. Create and activate a virtual environment (optional):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install fastapi uvicorn pytz
    ```

4. Run the application:
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    ```

5. The API will be available at `http://127.0.0.1:8000/`.

## API Documentation

### Endpoint
#### `GET /`

**Request:**
```http
GET / HTTP/1.1
Host: your-api-endpoint
