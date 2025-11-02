from internetMarket.domain.models import Product


class ProductRepository:
    def __init__(self):
        self.products = []
        self.next_id = 1

    def add_product(self, name: str, price: float) -> Product:
        product = Product(id=self.next_id, name=name, price=price)
        self.products.append(product)
        self.next_id += 1
        return product

    def list_products(self):
        return self.products