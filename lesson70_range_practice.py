# 1 Вариант использования диапазона в цикле
my_range = range(5)

for n in my_range:
    print(n)

# 2 Вариант использования диапазона в цикле
for n in range(5):
    print(n)

# 3 Вариант использования диапазона в цикле
for n in range(12, 25, 5):
    print(n)

# Различная конвертация
print(set(range(12, 25, 5)))
print(list(range(12, 25, 5)))
print(tuple(range(12, 25, 5)))

# Методы диапазона. У диапазонов только два метода: count(), index()
my_ran = range(10, 30, 3)
# Посмотреть все методы print(dir(my_ran))
print(my_ran.count(13))

# Задание
ex_range = range(10, 101, 5)

my_list = []
for n in ex_range:
    my_list.append(n)

print(my_list)
