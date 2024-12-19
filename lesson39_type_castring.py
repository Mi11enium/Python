# Type casting or type conversion
# Python НЕ ВЫПОЛНЯЕТ неявную конвертацию типов значений

# Встроенные функции для явной конвертации типов
# str(), float(), tuple(), int(), list(), set(), ...


# Операции с значениями разных типов
# '10' + 5  TypeError: can only concatenate str (not 'int) to str

# Порядок операндов имеет значение
# 5 + '10' TypeError: unsupported operand types(s) for +: 'int' and 'str'


# Явная конвертация типа одного из значений
print(5 + int('10'))


int_num = 5
float_num = 4.5

print(int_num + float_num)
print(float_num + int_num)

bool_val = True
int_val = 7

print(bool_val + int_val)
print(int_val + bool_val)
