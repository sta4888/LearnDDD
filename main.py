from fastapi import FastAPI

from fastapiMarket.application.services import ShopService

app = FastAPI()
service = ShopService()

@app.get("/products")
def list_products():
    return service.list_products()

@app.post("/products")
def add_product(name: str, price: float):
    return service.add_product(name, price)

@app.post("/orders")
def create_order():
    return service.create_order()

@app.post("/orders/{order_id}/add_item")
def add_item(order_id: int, product_id: int, quantity: int):
    service.add_item_to_order(order_id, product_id, quantity)
    return {"status": "ok"}
