my_set = {'f', 'd'}
other_set = {'d', 'f'}

print(my_set.intersection('abcd'))

print(my_set.issuperset(other_set))

print(my_set == other_set)

# Удалять элементы из набора межно с помощью метода discard()
my_set = {1, 2, 3}

print(my_set.discard(3))  # None

print(my_set)  # {1, 2}
