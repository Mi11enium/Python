db_is_available = False

print(db_is_available)
print(type(db_is_available))

db_is_available = True
print(db_is_available)


print(bool(10))
print(bool('abc'))
print(bool([1, 2]))
print(bool([]))
print(bool({}))
print(bool(None))


print(100 > 10)
# Тут False, потому что выполняется посимвольное сравнение
print('Long string' > 'Short')
print([] == [])
print({'a': 3, 'b': 5} == {'a': 3, 'b': 5})
