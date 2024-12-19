# Копирование списка

# В этом случае оригинал переменной my_cars изменяется т.к.
# copied_cars = my_cars является копированием по ссылке.
my_cars = ['BMW', 'Mercedes']

copied_cars = my_cars

copied_cars.append('Audi')

print(copied_cars)  # ['BMW', 'Mercedes', 'Audi']
print(my_cars)  # ['BMW', 'Mercedes', 'Audi']

print((id(my_cars)) == id(copied_cars))

# (1)
# В этом случае оригинал переменной my_cars НЕ изменяется т.к.
# copied_cars = my_cars[:] НЕ является копированием по ссылке.
# Создание нового списка, используя slice
my_cars = ['BMW', 'Mercedes']

copied_cars = my_cars[:]

copied_cars.append('Audi')

print(copied_cars)  # ['BMW', 'Mercedes', 'Audi']
print(my_cars)  # ['BMW', 'Mercedes']

print((id(my_cars)) == id(copied_cars))

# (2)
# В этом случае оригинал переменной my_cars НЕ изменяется т.к.
# copied_cars = my_cars.copy() НЕ является копированием по ссылке.
# Создание нового списка, используя slice
my_cars = ['BMW', 'Mercedes']

copied_cars = my_cars.copy()  # Предпочтительный вариант использования в работе

copied_cars.append('Audi')

print(copied_cars)  # ['BMW', 'Mercedes', 'Audi']
print(my_cars)  # ['BMW', 'Mercedes']

print((id(my_cars)) == id(copied_cars))

# (3)
# В этом случае оригинал переменной my_cars НЕ изменяется т.к.
# copied_cars = my_cars.copy() НЕ является копированием по ссылке.
# Создание нового списка, используя функцию list()
my_cars = ['BMW', 'Mercedes']

copied_cars = list(my_cars)

copied_cars.append('Audi')

print(copied_cars)  # ['BMW', 'Mercedes', 'Audi']
print(my_cars)  # ['BMW', 'Mercedes']

print((id(my_cars)) == id(copied_cars))
