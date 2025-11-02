from dataclasses import dataclass, field
from typing import List

@dataclass
class Product:
    id: int
    name: str
    price: float


@dataclass
class OrderItem:
    product: Product
    quantity: int

    def total_price(self) -> float:
        return self.product.price * self.quantity


@dataclass
class Order:
    id: int
    items: List[OrderItem] = field(default_factory=list)

    def add_item(self, product: Product, quantity: int):
        self.items.append(OrderItem(product, quantity))

    def total_price(self) -> float:
        return sum(item.total_price() for item in self.items)