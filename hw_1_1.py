from queue import Queue
import time

# Створити чергу заявок
queue = Queue()

id_i = 1
def generate_request():
    global id_i
    new_order = {"id": id_i}
    queue.put(new_order)
    id_i += 1

# Якщо черга не пуста:
#     Видалити заявку з черги
#     Обробити заявку
# Інакше:
#     Вивести повідомлення, що черга пуста
def process_request():
    if queue.empty():
        return print('Queue is empty')

    order = queue.get()
    print(f"Обробка заявки {order['id']}")

# Головний цикл програми:
#     Поки користувач не вийде з програми:
#         Виконати generate_request() для створення нових заявок
#         Виконати process_request() для обробки заявок

if __name__ == "__main__":
    while True:
        generate_request()
        process_request()
        time.sleep(0.1)
    