from dataclasses import dataclass, field
from typing import List

@dataclass
class Product:
    id: int
    name: str
    price: float


@dataclass
class OrderItem:
    id: int
    product_id: int
    quantity: int
    price: float  # цена на момент заказа


@dataclass
class Order:
    id: int
    items: List[OrderItem] = field(default_factory=list)

    def total_price(self) -> float:
        return sum(item.price * item.quantity for item in self.items)
