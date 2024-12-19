# Элементы, которых нет в пересечении множеств. symmetric_difference()

a = {'abc', 'd', 'f', 'y'}
b = {'abc', 'd', 'f', 'l'}

# symmetric_difference это тажке union - inter

print((a | b) - (a & b))
