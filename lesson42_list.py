# list
# Список является изменяемым объектом
# Список - это УПОРЯДОЧЕННАЯ последовательность элементов
# это значит, что порядок элементов в списке играет роль - у каждого элемета
# в списке есть свой уникальный индекс. Индексы начинаются с 0


my_fruits = ['apple', 'banana', 'lime']
other_fruits = ['banana', 'apple', 'lime']

print(my_fruits == other_fruits)

# Получение значений
posts_ids = [151, 245, 762, 167]

print(posts_ids[0])  # 151
print(posts_ids[1])  # 245
print(posts_ids[-1])  # Получение последнего элемента 167

# Изменение значений
posts_ids[0] = 555
posts_ids[2] = 333

print(posts_ids)  # 555, 245, 333, 167

# Удаление значений
print(len(my_fruits))  # 3

del my_fruits[0]
print(my_fruits)  # 'banana', 'lime'

del other_fruits[-1]
print(other_fruits)  # 'banana', 'apple'

# Список словарей
users = [
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 831,
        'user_name': 'Bob'
    }
]

print(len(users))
print(users[1]['user_id'])  # 831 ## Получение к значению через ключ словаря

# Использование переменных
my_fruit = 'apple'
other_fruit = 'banana'
new_fruit = 'lime'

all_fruits = [my_fruit, other_fruit, new_fruit]
print(all_fruits)  # 'apple', 'banana', 'lime'
