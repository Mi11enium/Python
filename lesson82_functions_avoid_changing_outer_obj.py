# Внутри функции НЕ РЕКОМЕНДУЕТСЯ изменять внешние объекты (это относится к set, list, dict)
# Чтобы это избежать, нужно создать копию объекта


def increase_person_age(person):
    person_copy = person.copy()
    person_copy['age'] += 1
    return person_copy

person_one = {
    'name': 'Bob',
    'age': 21
}

new_person = increase_person_age(person_one)
print(new_person['age'])  #  22
print(person_one['age'])  #  21