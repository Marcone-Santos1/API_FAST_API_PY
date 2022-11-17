from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {
        "id": 1,
        "name": "TV",
        "price": 1000,
        "brand": "Samsung",
        "quantity": 10
    }
}

@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    if product_id in vendas:
        return (
            vendas[product_id]
        )
    else:
        return {"Error": "Product not found"}

@app.get("/products")
def get_all_product():
    return (
        vendas
    )
    
@app.post("/products")
def create_product(product: dict):
    vendas[product["id"]] = product
    return (
        vendas
    )

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    if product_id in vendas:
        del vendas[product_id]
        return (
            vendas
        )
    else:
        return {"Error": "Product not found"}
    
@app.put("/products/{product_id}")
def update_product(product_id: int, product: dict):
    if product_id in vendas:
        vendas[product_id] = product
        return (
            vendas
        )
    else:
        return {"Error": "Product not found"}