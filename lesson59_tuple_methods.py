# У кортежей есть только два метода: count(), index()
# count() - подсчет количества определенных элементов
# index() - поиск индекса по имени элемента
# Методы кортежей наследуются от класса tuple

# count()
posts_ids = (151, 245, 762, 245)

print(posts_ids.count(245))  # 2

print(posts_ids.count(151))  # 1

# index() ;Если элемент попадается несколько раз, то возвращается первое соответствие
print(posts_ids.index(245))  # 1

print(posts_ids.index(762))  # 2

# Конвертация в список
phone_ids = (151, 245)

phone_ids_list = list(phone_ids)
phone_ids_list.append(351)

print(phone_ids_list)  # [151, 245, 351]

# Конвертация списка в кортеж
phone_ids_tuple = tuple(phone_ids_list)

print(phone_ids_tuple)  # (151, 245, 351)
