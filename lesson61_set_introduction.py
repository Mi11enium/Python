# Набор - это неупорядоченная последовательность элементов
# Набор содержит только УНИКАЛЬНЫЕ элементы
# Изменять наборы МОЖНО
# В наборах обычно сохраняют однотипные данные (только строки, числа...)

# Структура и синтаксис
my_fruits = {'apple', 'banana', 'lime'}

posts_ids = {151, 245, 762, 167}

# Могут быть различные типы, но обычно так не делают
user_inputs = {True, 'hi', 25, 10.5}

print(my_fruits)  # {'banana', 'apple', 'lime'}

print(type(my_fruits))  # <class 'set'>

# Особенность наборов - уникальные элементы
posts_ids = {151, 245, 167, 167, 151}

print(posts_ids)  # {151, 245, 167}

print(type(posts_ids))

# Порядок элементов в наборах не важен. т.к. элементы неупорядочены -
# индексов у них нет
my_guitar = {'esp', 'jackson', 'fender'}
other_guitars = {'fender', 'esp', 'jackson'}

print(my_guitar == other_guitars)  # True

# Длина набора. len()
my_fruits = {'apple', 'banana', 'lime'}
print(len(my_fruits))  # 3

posts_ids = {151, 245, 762, 167}
print(len(posts_ids))  # 4
