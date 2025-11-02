# LearnDDD





## internetMarket

| Слой               | Что делает                          | Пример                              |
| ------------------ | ----------------------------------- | ----------------------------------- |
| **Domain**         | Правила мира (товар, заказ, логика) | `Product`, `Order`, `total_price()` |
| **Application**    | Управляет процессом                 | `OrderService`                      |
| **Infrastructure** | Хранит данные                       | `ProductRepository`                 |
| **Interface**      | Общается с пользователем            | `main.py`                           |
