# Копирование словаря. Метод copy(). Используем, когда хотим сделать какие-то
# операции со словарем, но при этом не изменять оригинальный словарь.

my_disk = {
    'brand': 'Samsung',
    'price': 80,
}

my_disk.copy()

new_disk = my_disk.copy()

new_disk['type'] = 'ssd'

print(my_disk)
print(new_disk)
print(id(my_disk))
print(id(new_disk))

print(len(my_disk))
