# My API Project

This is a sample API project using FastAPI. It provides endpoints to retrieve a list of discounted products with optional filters and pagination.

## Features

- Retrieve a list of discounted products
- Filter products by store, category, and minimum discount percentage
- Support for pagination

## Endpoints

- `GET /discounted-products`: Retrieve a list of discounted products with optional filters and pagination.

## How to Run the Project

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run Alembic migrations**:
    ```sh
    alembic upgrade heads
    ```

4. **Run the FastAPI application**:
    ```sh
    uvicorn main:app --reload
    ```

5. **Run the crawler**:
    ```sh
    python run_crawler.py
    ```

6. **Access the API documentation**:
    - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


## Example Usage

```sh
GET /discounted-products?store=example&category=electronics&min_discount=10&skip=0&limit=10