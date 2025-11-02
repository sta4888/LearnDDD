from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///shop.db", echo=False)
SessionLocal = sessionmaker(bind=engine)

class ProductDB(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)

class OrderDB(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    items = relationship("OrderItemDB", back_populates="order")

class OrderItemDB(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    price = Column(Float)
    order = relationship("OrderDB", back_populates="items")


# class UserDB(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     login = Column(String)
#     password = Column(String)
#     orders = relationship("OrderDB", back_populates="user")

Base.metadata.create_all(bind=engine)
