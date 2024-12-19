# Несуществующие ключи

my_motorbike = {
    'brand': 'ducati',
    'price': 26400,
    'engine_vol': 1.2,
}

# print(my_motorbike['model'])  # KeyError: 'model', такого ключа в словаре нет

# Использование метода get для получения значений ключей. Если ключа нет, то
# программа не остановится, а выполнит None.
# Таким образом происходит обход ошибки ключа, если ключа в словаре нет.
# Это нужно делать тогда, когда мы не знаем есть ли нужный нам ключ в словаре.

print(my_motorbike.get('model'))  # None
print(my_motorbike.get('tank', 0))  # Здесь вторым аргументом мы вписываем
# возвращающее значение в случае осутствия ключа