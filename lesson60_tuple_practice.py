my_nums = (10, 5, 100, 0, 5, 5)

print(my_nums.index(5))

# Нахождение последующих индексов, кроме первого входящего
index_one = my_nums.index(5)  # 1
index_two = my_nums.index(5, index_one + 1)  # 4
index_three = my_nums.index(5, index_two + 1)  # 5

print(index_three)

# Конвертация в список + добавление элемента
my_list = list(my_nums)

my_list.append(7)

print(my_list)

# Обратная конвертация списка в кортеж

my_nums = tuple(my_list)

print(my_nums)

# При конвертации строки, мы получаем разделение строки на элементы
my_tuple = tuple('abcd')
print(my_tuple)  # ('a', 'b', 'c', 'd')

# При конвертации в список мы получаем только ключи
my_dict = tuple({'first': 1, 'second': 2})
print(my_dict)  # ('first', 'second')
