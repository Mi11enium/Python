# Функция zip позволяет формировать новые объекты на основании других
# последовательностей т.е. объединять последовательности вместе

# Выводим два списка для слияния
fruits = ['apple', 'banana', 'lime']
quantities = [100, 70, 50]

# Используем функцию zip. Она выводит адрес объекта в памяти
fruit_qtys_zip = zip(fruits, quantities)

print(fruit_qtys_zip)  # <zip object at 0x000001C8BE4F1500>
print(type(fruit_qtys_zip))
# Конвертируем zip-объект и получаем список кортежей
fruit_qtys_list = list(fruit_qtys_zip)

print(fruit_qtys_list)  # [('apple', 100), ('banana', 70), ('lime', 50)]
print(type(fruit_qtys_list))
