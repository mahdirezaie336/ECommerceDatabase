# main.py
from fastapi import FastAPI
from routes.product import router as product_router

app = FastAPI()

app.include_router(product_router, prefix="", tags=["products"])


@app.get("/")
async def root():
    return {"message": "Hello World"}

