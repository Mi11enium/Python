
my_list = [0, True, 'abc']
# Чтобы сконвертировать список в словарь, его необходимо дополнить, сделав
# Из него список списков
my_list = [['first', 0], ['second', True], ['Third', 'abc']]
# Либо список из кортежей
my_list = [('first', 0), ('second', True), ('Third', 'abc')]


my_dict = dict(my_list)
print(my_list)
