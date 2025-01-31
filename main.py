from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():
    utc_time = datetime.utcnow().isoformat(timespec="seconds") + "Z"
    return {
        "email": "abasiomofonudoh@gmail.com",
        "current_datetime": utc_time,
        "github_url": "https://github.com/omofz/stage0-hng"
    }
