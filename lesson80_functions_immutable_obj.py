# Передача неизменяемых объектов
# При манипуляциях с неизменяемыми объектами, создается новый объект

def my_fn(a, b):
    a = a + 1
    c = a + b
    return c

num_one = 10
num_two = 5

res = my_fn(num_one, num_two)
print(res)  # 16
print(num_one)  # 10 ## значение переменной не изменилось