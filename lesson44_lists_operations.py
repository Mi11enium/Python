# Конвертация в список
greeting = "Hello from Python"
greeting_letters = list(greeting)

print(greeting_letters)
# ['H', 'e', 'l', 'l', 'o', ' ', 'f', 'r', 'o', 'm', ' ', 'P', 'y', 't', 'h', 'o', 'n']

my_dict = {'a': 10, 'b': True}
my_dict_keys = list(my_dict)

print(my_dict_keys)
# ['a', 'b'] ## Здесь мы получаем только ключи, значения утериваются

# Арифметические операции в списках
ratings = [2.5, 5.0, 4.3, 3.7]

print(min(ratings))  # 2.5
print(max(ratings))  # 5.0
print(sum(ratings))  # 15.5

print((sum(ratings))/len(ratings))  # 3.875

# Объединение списков
my_ratings = [2.5, 5.0]
other_ratings = [3.7, 4.5, 4.9]

all_ratings = my_ratings + other_ratings

print(all_ratings)

# Нарезка списков
ratings = [2.5, 2.0, 4.3, 3.7, 4.5]

first_two_ratings = ratings[:2]
print(first_two_ratings)  # [2.5, 2.0]

middle_ratings = ratings[1:-1]
print(middle_ratings)  # [2.0, 4.3, 3.7]

last_two_ratings = ratings[-2:]
print(last_two_ratings)  # [3.7, 4.5]
