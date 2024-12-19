# Конвертация zip объекта в словарь

fruits = ['apple', 'banana', 'lime']

quantities = [100, 70, 50]

# (1) fruits - keys, (2) qties - values
fruit_qtys_zip = zip(fruits, quantities)

print(fruit_qtys_zip)  # <zip object at 0x000001AD30C81500>

fruit_qtys_dict = dict(fruit_qtys_zip)

print(fruit_qtys_dict)  # {'apple': 100, 'banana': 70, 'lime': 50}
