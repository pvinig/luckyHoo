from fastapi import FastAPI
from fastapi import routing
from Routes.MainRoutes import api
import uvicorn

app = FastAPI()
app.include_router(api)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
