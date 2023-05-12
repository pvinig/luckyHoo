from fastapi import FastAPI
from src.Routes.user import api
import uvicorn

app = FastAPI()
app.include_router(api)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
