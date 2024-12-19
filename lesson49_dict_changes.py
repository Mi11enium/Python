# Получение значений
# Для словарей ключи не являются атрибутами! К ним нельзя обратиться через точку
# Для получения атрибутов словаря используется функция dir()

my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2
}

print(my_motorbike['brand'])  # Ducati
print(my_motorbike['price'])  # 25000
print(my_motorbike['engine_vol'])  # 25000


# Изменение значений
my_motorbike = {
    'brand': 'honda',
    'price': 10000,
    'engine_vol': 2.4,
}

my_motorbike['price'] = 15000

print(my_motorbike['price'])

# Добавление новых элементов
my_motorbike['new_elem'] = True
print(my_motorbike)

# Удаление элементов
del my_motorbike['engine_vol']
print(my_motorbike)
