from infrastructure.repositories import ProductRepository
from application.services import OrderService

# создаём "базу" товаров
repo = ProductRepository()
apple = repo.add_product("Яблоко", 1.5)
banana = repo.add_product("Банан", 2.0)

# создаём сервис заказов
service = OrderService()
order = service.create_order()

# добавляем товары в заказ
service.add_product_to_order(order, apple, 3)
service.add_product_to_order(order, banana, 2)

# считаем сумму
print("Ваш заказ:")
for item in order.items:
    print(f"- {item.product.name} x{item.quantity} = {item.total_price()} руб.")

print(f"Итого: {service.calculate_total(order)} руб.")