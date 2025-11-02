from fastapiMarket.domain.models import Order
from fastapiMarket.infrastructure.repositories import ProductRepository, OrderRepository


class ShopService:
    def __init__(self):
        self.products = ProductRepository()
        self.orders = OrderRepository()

    def list_products(self):
        return self.products.list_all()

    def add_product(self, name: str, price: float):
        return self.products.add(name, price)

    def create_order(self) -> Order:
        return self.orders.create_order()

    def add_item_to_order(self, order_id: int, product_id: int, quantity: int):
        product = next(p for p in self.products.list_all() if p.id == product_id)
        self.orders.add_item(order_id, product, quantity)
