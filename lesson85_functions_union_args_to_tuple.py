# Объединение всех аргументов в кортеж в функции
# Может ли функция принимать любое количество аргументов? Да. В виде кортежа.

# Объединение аргументов в tuple

def sum_nums(*args):  # с помощью звёздочки происходит объединение всех позиционных аргументов в один кортеж
    print(args)  # (2, 3, 7)
    print(type(args))  # <class 'tuple'>
    print(args[0])
    return sum(args)

print(sum_nums(2, 3, 7))