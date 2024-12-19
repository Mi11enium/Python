# Последовательности: сравнение типов
# Тип данных	Изменяемый?	Упорядоченный?	Может содержать одинаковые элементы?
# int, float	Нет	Нет	Не применимо
# str	Нет	Да	Да
# list	Да	Да	Да
# tuple	Нет	Да	Да
# set	Да	Нет	Нет
# dict	Да	Нет	Ключи - нет, значения - да
# range	Нет	Да	Нет

num = 10
n_float = 9.5
my_str = 'hello'

# list
my_list = [1, 2, 3]
my_list.append(6)
my_list[2] = 4
my_list.append(6)
print(my_list)

# tuple
my_tuple = (1, 2, 3, 3)
# --
print(my_tuple[0])
print(my_tuple)

# set
my_set = {1, 2, 3}
my_set3 = my_set & {3, 4, 5}
# --
# --
print(my_set3)

# dict
my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3
# --
my_dict['d'] = 3

print(my_dict)

# range
my_range = range(5)
# --
print(my_range[2])
# --
