
my_disk = {}

# print(id(my_disk))
# print(type(my_disk))

my_disk['brand'] = 'Samsung'
my_disk['price'] = 80
my_disk['gate'] = '25'

# print(my_disk)
# print(id(my_disk))

# При вызове метода items() возвращается список, который имеет пары ключ-значение
# каждая пара это тип touple (кортеж)
print(my_disk.items())  # dict_items([('brand', 'Samsung'), ('price', 80)])
print(type(my_disk.items()))  # <class 'dict_items'>


# Создание экземпляра класса в виде списка с типом dict_keys
print(my_disk.keys())  # dict_keys(['brand', 'price'])
print(type(my_disk.keys()))  # <class 'dict_keys'>

# Удаление последнего входящего элемента (пары ключ-значение)
# Его использование НЕ РЕКОМЕНДУЕТСЯ!
# Лучше использовать оператор del
print(my_disk.popitem())

print(my_disk.get('gate', 'hdd'))
