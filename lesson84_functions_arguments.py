# Аргументы функции
# Позиционные аргументы my_fn(a, b) - их порядок важен!
# Если у функции определены два параметра, то при вызове функции нужно обязательно передавать два аргумента!

def my_fn(a, b):  # Здесь у нас a, b - параметры. Параметры - это переменные, которые доступны внутри функции (в скобках)
    a = a + 1
    c = a + b
    return c

my_fn(10, 3)  # Здесь у нас a, b - аргументы. Аргументы могут изменяться при каждом вызове функции

# Позиционные аргументы
def get_posts_info(name, posts_qty):
    info = f"{name} wrote {posts_qty} posts"
    return info

info = get_posts_info('Bogdan', 25)
print(info)


# Ошибка отсутствия аргументов
def sum_nums(a, b):
    c = a + b
    return c

print(sum_nums(2, 5))
# print(sum_nums(2))  # TypeError: sum_nums() missing 1 required positional argument: 'b'
# print(sum_nums())  # TypeError: sum_nums() missing 2 required positional arguments: 'a' and 'b'


# Ошибка чрезмерного количества аргументов
def sum_nums(a, b):  # При вызове этой функции нужно передавать ТОЧНО два аргумента
    c = a + b
    return c

# print(sum_nums(2, 3, 5))  # TypeError: sum_nums() takes 2 positional arguments but 3 were given
