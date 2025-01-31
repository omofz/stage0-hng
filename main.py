import datetime
import  pytz
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    lagos_time = datetime.datetime.now(pytz.timezone('Africa/Lagos'))
    return {
            "email": "your-email@example.com",
            "current_datetime": f"{lagos_time}",
            "github_url": "https://github.com/omofz/stage0-hng"
        }