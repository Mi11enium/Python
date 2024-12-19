# После копирования ИЗМЕНЯЕМЫХ объектов изменения отражаются на ВСЕХ объектах
# Адреса ИЗМЕНЯЕМЫХ объектов

my_list = [1, 2, 3]
print(id(my_list))  # 2971668568320

other_list = [1, 2, 3]
print(id(other_list))  # 2971668566400

print(id([1, 2, 3]))  # 2971668887680

# Пример операции с изменяемыми объектами

my_list = [1, 2, 3]  #
other_list = [1, 2, 3]  #

other_list.append(4)

print(my_list)  # [1, 2, 3]
print(other_list)  # [1, 2, 3, 4]

# Пример со словарем

info = {
    'name': 'Anatolii',
    'is_instructor': False
}

info_copy = info

info['reviews_qty'] = 5

print(info['reviews_qty'])  # 5
print(info_copy['reviews_qty'])  # 5

# Второй пример со словарем

info = {
    'name': 'Anatolii',
    'is_instructor': False
}

info_copy = info

info['reviews_qty'] = 5
info_copy['reviews_qty'] = 100

print(info['reviews_qty'])  # 100
print(info_copy['reviews_qty'])  # 100

# Третий пример со словарем

info = {
    'name': 'Anatolii',
    'is_instructor': False
}

other_info = {
    'name': 'Anatolii',
    'is_instructor': False
}
