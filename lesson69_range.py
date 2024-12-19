# Диапазон - упорядоченная неизменяемая последовательность элементов
# Диапазоны обычно используются в циклах
# Создание my_range = range(end_num) or my_range = (start, stop, step)
# stop не включительно

# Структура и синтаксис
my_range = range(7)

print(type(my_range))  # <class 'range'>

print(my_range)  # range(0, 7)

print(list(my_range))  # [0, 1, 2, 3, 4, 5, 6]

my_range2 = range(10, 20, 3)  # start, stop, step

print(my_range2)  # range(10, 20, 3)

print(list(my_range2))  # [10, 13, 16, 19]

# Индексы элементов в диапазонах

print(my_range2[0])  # 10
print(my_range2[1])  # 13
print(my_range2[2])  # 16
print(my_range2[3])  # 19

# Использование диапазонов в циклах
my_range2 = range(10, 20, 3)  # start, stop, step

for n in my_range2:
    print(n)  # 10, 13, 16, 19
