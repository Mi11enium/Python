# При использовании методов вспоминаем про множества (пересекающиеся круги)
# Методы наборов наследуются от класса set
# add(), union(), remove(), difference(), intersection(), discard(), clear()
# copy(), update(), issubset(), issuperset(), pop() ...

# Добавление новых элементов. add()

photo_sizes = {'1920x1080', '800x600'}

photo_sizes.add('1024x768')

print(photo_sizes)  # {'800x600', '1920x1080', '1024x768'}

# Объединение наборов (получение всех уникальных элементов). union()
photo_sizes = {'1920x1080', '800x600'}
other_sizes = {'800x600', '1024x768'}

all_sizes = photo_sizes.union(other_sizes)

print(all_sizes)  # {'1024x768', '800x600', '1920x1080'} ## дубль удален

# Также можно использовать оператор |
all_sizes2 = photo_sizes | other_sizes
print(all_sizes2)  # {'800x600', '1024x768', '1920x1080'}

# Пересечение наборов. intersection()
photo_s = {'1920x1080', '800x600'}
other_s = {'800x600', '1024x768'}

common_s = photo_s.intersection(other_s)

print(common_s)  # {'800x600'}

# Также можно использовать оператор &
common_s2 = photo_s & other_s
print(common_s2)

# Разность наборов. difference()
dif_set1 = {1, 2, 3}
dif_set2 = {3, 4, 5}

dif_total = dif_set1.difference(dif_set2)

print(dif_total)  # {1, 2}

# Также можно использовать оператор -
dif_total2 = dif_set1 - dif_set2

print(dif_total2)  # {1, 2}

# Симметрическая разность наборов. difference()
sym_set1 = {1, 2, 3}
sym_set2 = {3, 4, 5}

sym_total = sym_set1.symmetric_difference(sym_set2)

print(sym_total)  # {1, 2, 4, 5}

# Также можно использовать оператор ^
sym_total2 = sym_set1 ^ sym_set2

print(sym_total2)  # {1, 2, 4, 5}


# Включение одного набора в другой. issubset()
nums = {10, 5, 35}
other_nums = {20, 5, 12, 10, 35}

res = nums.issubset(other_nums)

print(res)  # True
