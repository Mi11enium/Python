# Переменная содержит ссылку на объект

# Получение адреса объекта
my_country = 'russia'
print(id(my_country))
my_country = 122
print(id(my_country))

# Переменные могут ссылаться на один объект в памяти
my_number = 10
print(id(my_number))
# 140730099505880
other_number = my_number
print(id(my_number))
# 140730099505880
