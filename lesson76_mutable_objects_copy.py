# Как избежать изменение копий
# Использовать метод copy()

info = {
    'name': 'Bogdan',
    'is_instructor': True
}

info_copy = info.copy()

info_copy['reviews_qty'] = 5

print(info_copy)  # {'name': 'Bogdan', 'is_instructor': True, 'reviews_qty': 5}

print(info)  # {'name': 'Bogdan', 'is_instructor': True}

# ЗДЕСЬ НУЖНО БЫТЬ ВНИМАТЕЛЬНЫМ!
# Если у словаря есть вложенные изменяемые объекты (list, dict, set), то ссылки на них !сохраняются!
# Если значения неизменяемые (числа, строки и т.д), то объект скопируется без одинаковых ссылок внутри


info = {
    'name': 'Bogdan',
    'is_instructor': True,
    'reviews': []
}

info_copy = info.copy()

info_copy['reviews'].append('Great course')

print(info)  # {'name': 'Bogdan', 'is_instructor': True, 'reviews': ['Great course']}

print(info_copy)  # {'name': 'Bogdan', 'is_instructor': True, 'reviews': ['Great course']}


# ТО ЕСТЬ
# ЕСЛИ В СЛОВАРЕ ЕСТЬ ИЗМЕНЯЕМЫЙ ОБЪЕКТ (list, dict, set), то при его копировании
# и изменении значения, у нас будет изменяться и оригинальный объект!

# Мы можем обойти сохранение всех ссылок используя встроенный модуль deepcopy

# Встроенный модуль deepcopy
from copy import deepcopy

info = {
    'name': 'Bogdan',
    'is_instructor': True,
    'reviews': []
}

info_deepcopy = deepcopy(info)

info_deepcopy['reviews'].append('Great course')

print(info)  # {'name': 'Bogdan', 'is_instructor': True, 'reviews': []}

print(info_deepcopy)  # {'name': 'Bogdan', 'is_instructor': True, 'reviews': ['Great course']}

