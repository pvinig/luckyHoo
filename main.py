from fastapi import FastAPI
from fastapi import routing
from Routes.MainRoutes import api

app = FastAPI()

app.include_router(api)