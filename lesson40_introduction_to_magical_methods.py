# Магические методы - это методы, которые вызываются при использовании операторов
# Порядок операндов важен!
# у класса int нет магического метода __radd__
# При использовании операторов python вызывает магические методы, при этом,
# в случае ошибки NotImplemented, python пробует менять операнды местами.

int_num = 5
float_num = 4.5

print(int_num + float_num)
# 9.5

# Магический метод __add__ класса int
print(int_num.__add__(float_num))
# NotImplemented

# Магический метод __radd__ класса float
print(float_num.__radd__(int_num))
# 9.5


int_num = 50
float_num = 7.5

# print(int_num * float_num)

print(int_num.__mul__(float_num))
# NotImplemented
print(float_num.__rmul__(int_num))
# 375.0


int_num = 50
str_val = 'abc'

# print(str_val * int_num)

print(int_num.__mul__(str_val))
# NotImplemented
print(str_val.__rmul__(int_num))
# abcabcabc...


float_num = 50.5
str_val = 'abc'

# print(float_num * str_val)

print(float_num.__mul__(str_val))
# NotImplemented
print(str_val.__rmul__(float_num))
# TypeError: 'float' object cannot be interpreted as an integer
