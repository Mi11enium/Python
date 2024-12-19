from copy import deepcopy

info = {
    'name': 'Bogdan',
    'is_instructor': True,
    'reviews': []
}

info_deepcopy = deepcopy(info)

info_deepcopy['reviews'].append('Great course')
info_deepcopy['reviews'].append('Great course')

info['reviews'].append('Super')
print(info)  # {'name': 'Bogdan', 'is_instructor': True, 'reviews': ['Super']}

print(info_deepcopy)  # {'name': 'Bogdan', 'is_instructor': True, 'reviews': ['Great course', 'Great course']}
