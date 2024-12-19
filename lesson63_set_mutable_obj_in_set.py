# Изменяемые объекты в наборах
# В наборы нельзя добавлять изменяемые объекты list, dict, set

lists_set = {[1, 2], [20, 5]}

print(lists_set)  # TypeError: unhashable type: 'list'
