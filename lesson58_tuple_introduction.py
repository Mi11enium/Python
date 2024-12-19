# Tuple - кортежи - упорядочнный, неизменяемый
# Кортеж - это упорядоченная последовательность элементов
# В отличие от списков, кортежи изменять нельзя - из него нельзя удалить или
# добавить в него новые элемениты.
# В кортежах могут быть объекты разных типов

# Структура и синтаксис
my_fruits = ('apple', 'banana', 'lime')

posts_ids = (151, 245, 762, 167)

user_inputs = (True, 'hi', ':smile:', 10.5)

# Порядок следования элементов в кортежах важен!

my_fruits = ('apple', 'banana', 'lime')
other_fruits = ('banana', 'apple', 'lime')
# В данном случае это будут разные кортежи
print(my_fruits == other_fruits)  # False

# Длина кортежа. len()
print(len(my_fruits))  # 3
print(len(posts_ids))  # 4
print(len(user_inputs))  # 4

# Получение значений элементов по ID
print(posts_ids[0])  # 151
print(posts_ids[1])  # 245
print(posts_ids[-1])  # 167

# Изменять значение в кортеже нельзя!
# posts_ids[0] = 555  # TypeError: 'tuple' object does not support item assignment
# del posts_ids[0]  # TypeError: 'tuple' object does not support item assignment

# Кортеж словарей
users = (
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 831,
        'user_name': 'Bob'
    }
)

print(users[1]['user_id'])  # 831 ## Получение значения из словаря

# Мы можем изменить значение, потому что изменяем значение в словаре
users[1]['user_id'] = 100

print(users[1]['user_id'])  # 100

# Использование переменных
my_fruit = 'apple'
other_fruit = 'banana'
new_fruit = 'lime'

all_fruits = (my_fruit, other_fruit, new_fruit)

print(all_fruits)  # ('apple', 'banana', 'lime')

# Объединение кортежей
internal_ids = (151, 245)
external_ids = (624, 451, 941)

all_ids = internal_ids + external_ids

print(all_ids)  # (151, 245, 624, 451, 941)
