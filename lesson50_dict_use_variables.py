
# Использование переменных в ключах

my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2,
}

key_name = 'brand'

my_motorbike[key_name] = 'BMW'

print(my_motorbike)  # 'brand': 'BMW', 'price': 25000, 'engine_vol': 1.2}

# Вложенные словари. Значением может быть словарь

my_motorbike = {
    'brand': 'Ducati',
    'engine_vol': 1.2,
    'price_info': {
        'price': 25000,
        'is_available': True
    }
}

print(my_motorbike['price_info']['price'])  # 25000
print(my_motorbike['price_info']['is_available'])  # True

# Использование переменных в значениях
brand = 'Ducati'
bike_price = 25000
engine_vol = 1.2

my_motorbike = {
    'brand': brand,
    'price': bike_price,
    'engine_vol': engine_vol,
}

print(my_motorbike)  # {'brand': 'Ducati', 'price': 25000, 'engine_vol': 1.2}
