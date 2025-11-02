from sqlalchemy.testing.pickleable import User

from .database import SessionLocal, ProductDB, OrderDB, OrderItemDB, UserDB
from ..domain.models import Product, Order


class ProductRepository:
    def __init__(self):
        self.db = SessionLocal()

    def add(self, name: str, price: float) -> Product:
        product_db = ProductDB(name=name, price=price)
        self.db.add(product_db)
        self.db.commit()
        self.db.refresh(product_db)
        return Product(id=product_db.id, name=product_db.name, price=product_db.price)

    def list_all(self):
        return [Product(id=p.id, name=p.name, price=p.price) for p in self.db.query(ProductDB).all()]


class OrderRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create_order(self) -> Order:
        order_db = OrderDB()
        self.db.add(order_db)
        self.db.commit()
        self.db.refresh(order_db)
        return Order(id=order_db.id)

    def add_item(self, order_id: int, product: Product, quantity: int):
        item_db = OrderItemDB(order_id=order_id, product_id=product.id, price=product.price, quantity=quantity)
        self.db.add(item_db)
        self.db.commit()


# class UserRepository:
#     def __init__(self):
#         self.db = SessionLocal()
#
#     def create_user(self) -> User:
#         user_db = UserDB()
#         self.db.add(user_db)
#         self.db.commit()
#         self.db.refresh(user_db)
#         return User(id=user_db.id)
#
#     def get_user_by_login(self, login: str) -> User:
#         user_db = self.db.query(UserDB).filter(UserDB.login == login).first()
#         return User(id=user_db.id, login=user_db.login)
