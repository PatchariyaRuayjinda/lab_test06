from fastapi import FastAPI
from routes.year_route import year_api_route

app = FastAPI() 

app.include_router(year_api_route)