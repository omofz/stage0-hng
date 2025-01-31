import datetime
import  pytz
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    utc_time = datetime.datetime.now(pytz.UTC).isoformat(timespec="seconds") + "Z"
    return {
        "email": "abasiomofonudoh@gmail.com",
        "current_datetime": utc_time,
        "github_url": "https://github.com/omofz/stage0-hng"
    }
