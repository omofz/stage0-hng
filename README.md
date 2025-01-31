<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FastAPI DateTime API</title>
</head>
<body>

    <h1>FastAPI DateTime API</h1>
    <p>A FastAPI application that provides the current date and time in ISO 8601 format (UTC) based on the Africa/Lagos timezone.</p>

    <h2>Features</h2>
    <ul>
        <li>Accepts <code>GET</code> requests.</li>
        <li>Returns the current date and time dynamically.</li>
        <li>Responds with an appropriate HTTP status code.</li>
        <li>Well-structured and documented code.</li>
        <li>Deployed to a publicly accessible endpoint.</li>
    </ul>

    <h2>Setup Instructions</h2>
    <h3>Prerequisites</h3>
    <p>Ensure you have the following installed:</p>
    <ul>
        <li>Python (>=3.7)</li>
        <li>pip</li>
        <li>Virtual environment (optional but recommended)</li>
    </ul>

    <h3>Installation</h3>
    <ol>
        <li>Clone the repository:</li>
        <pre><code>git clone https://github.com/omofz/stage0-hng.git
cd stage0-hng</code></pre>
        
        <li>Create and activate a virtual environment (optional):</li>
        <pre><code>python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`</code></pre>
        
        <li>Install dependencies:</li>
        <pre><code>pip install fastapi uvicorn pytz</code></pre>
        
        <li>Run the application:</li>
        <pre><code>uvicorn main:app --host 0.0.0.0 --port 8000 --reload</code></pre>
        
        <li>The API will be available at <code>http://127.0.0.1:8000/</code>.</li>
    </ol>

    <h2>API Documentation</h2>
    <h3>Endpoint</h3>
    <h4><code>GET /</code></h4>

    <p>Request:</p>
    <pre><code>GET / HTTP/1.1
Host: your-api-endpoint</code></pre>

    <p>Response:</p>
    <pre><code>{
    "email": "your-email@example.com",
    "current_datetime": "2024-07-10T12:00:00",
    "github_url": "https://github.com/omofz/stage0-hng"
}</code></pre>

    <h3>Example Usage</h3>

    <p>Using <code>curl</code>:</p>
    <pre><code>curl -X GET http://127.0.0.1:8000/</code></pre>

    <p>Using Python <code>requests</code>:</p>
    <pre><code>import requests
response = requests.get("http://127.0.0.1:8000/")
print(response.json())</code></pre>

    <h2>Deployment</h2>
    <p>The API should be deployed to a cloud service like Heroku, Vercel, or DigitalOcean to ensure it is publicly accessible.</p>

    <h2>Related Resources</h2>
    <p>For more Python developers, visit:</p>
    <p><a href="https://hng.tech/hire/python-developers">HNG Python Developers</a></p>

</body>
</html>
