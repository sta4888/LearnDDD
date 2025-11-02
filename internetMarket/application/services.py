from internetMarket.domain.models import Order, Product


class OrderService:
    def __init__(self):
        self.orders = []
        self.next_id = 1

    def create_order(self) -> Order:
        order = Order(id=self.next_id)
        self.next_id += 1
        self.orders.append(order)
        return order

    def add_product_to_order(self, order: Order, product: Product, quantity: int):
        order.add_item(product, quantity)

    def calculate_total(self, order: Order) -> float:
        return order.total_price()