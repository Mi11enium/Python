# В наборах нельзя получить значение элемента по индексу.
posts_ids = {10, 25, 16, 73}

# posts_ids[0]  # TypeError: 'set' object is not subscriptable
# Эта ошибка возникает если у объекта нет магического метода __getitem__()

posts_ids

posts_ids2 = [10, 25, 16, 73]

# posts_ids[0]  # TypeError: 'set' object is not subscriptable
# Эта ошибка возникает если у объекта нет магического метода __getitem__()

print(posts_ids2.__getitem__(0))  # 10

print(posts_ids2[0])  # 10

print(posts_ids2.__getitem__(0) == posts_ids2[0])

# Это значит, что у всех упорядоченных объектов есть магический метод __getitem()__
# Также __getitem__ выполняет функцию вывода значений по ключу в словарях
