# Методы списков
# Методы списков объекты наследуют от класса list
# append, pop, remove, insert, sort, index, clear, copy, extend, reverse, count

# append - добавление нового элемента в конец списка

happy_smiles = []

happy_smiles.append('😀')
happy_smiles.append('😃')
happy_smiles.append('😄')
happy_smiles.append('😁')

print(len(happy_smiles))  # 4

# pop - удаление элемента. если без аргументов, то последний элемент

inputs = [True, 'hi!', 42]
print(inputs)

inputs.pop(0)  # removed True
print(inputs)  # 'hi!', 42

removed_element = inputs.pop()  # removed 42
print(removed_element)

print(inputs)  # 'hi!'

# sort - сортировка элементов

posts_ids = [245, 151, 762, 167]

posts_ids.sort()

print(posts_ids)  # 151, 167, 245, 765

posts_ids.sort(reverse=True)
print(posts_ids)  # 762, 245, 167, 151
