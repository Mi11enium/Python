# Создать пустой словарь
my_dict = {}

# Трижды попросить пользователя сначала ввести название ключа,
# а потом ввести значение этого ключа. Всего должно быть 6 запросов на ввод текста
# не забываем что входные данные всегда в формате string
name_key1 = input('Введите название первого ключа: ')
name_value1 = bool(input('Введите название первого значения: '))
name_key2 = input('Введите название второго ключа: ')
name_value2 = input('Введите название второго значения: ')
name_key3 = input('Введите название третьего ключа: ')
name_value3 = input('Введите название третьего значения: ')


my_dict[name_key1] = name_value1
my_dict[name_key2] = name_value2
my_dict[name_key3] = name_value3


# Добавить новые ключи и значения
my_dict['new_atr'] = True
my_dict['new_prop'] = 28

# Удалить ключи
del my_dict['new_prop']


print(my_dict)
