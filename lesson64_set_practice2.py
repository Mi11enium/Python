# Удалять элементы с помощью del в наборах нельзя!

photo_dimensions = {'1920x1080', '800x600'}
print(len(photo_dimensions))  # 2

# del photo_dimensions[1]  # TypeError: 'set' object doesn't support item deletion

my_set = {10, 10, 5, 15, 15}

print(my_set)  # {10, 5, 15}
print(len(my_set))  # 3

# Для удаления используем методы remove() или discard()(метод с проверкой)
my_set.discard(10)
print(my_set)  # {5, 15}

# my_set2 = {[10, 10], 5, 15, 15}  # TypeError: unhashable type: 'list'
# Тут нет ошибки, потому что кортеж является неизменяемым
my_set3 = {(10, 10), 5, 15, 15}


# Создание пустого набора
# my_set = {} создаст словарь, а не набор
# Создание пустого набора. Это функция-конструктор, с помощью которой создается
# экземпляр класса set
my_set = set()

print(type(my_set))  # <class 'set'>
