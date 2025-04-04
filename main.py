from fastapi import FastAPI
from routes.product import router as product_router

app = FastAPI(
    title="My API",
    description="This is a sample API using FastAPI",
    version="1.0.0",
    contact={
        "name": "Your Name",
        "url": "http://example.com/contact",
        "email": "yourname@example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.include_router(product_router, prefix="", tags=["products"])


@app.get("/")
async def root():
    return {"message": "Hello World"}

