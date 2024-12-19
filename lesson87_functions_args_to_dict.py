# Объединение аргументов в словарь
# Для этого используется две звездочки перед названием параметра
# В таком случае передавать можно только ИМЕНОВАННЫЕ (name='Bogdan') аргументы (не позиционные!)

def get_posts_info (**person):
    print(person)

    print(type(person))  # <class 'dict'>
    info = (
        f"{person['name']} wrote"  # Если здесь не ставить запятую, python авт объеденит строки, т.е. это не кортеж
        f"{person['posts_qty']} posts"
    )
    return info

info = get_posts_info(name='Bogdan', posts_qty=25)
print(info)

# SUMMARY
# В python можно передавать как позиционные аргументы, так и аргументы с ключевыми словами
# Позиционные аргументы с помощью оператора * можно объединять в кортеж
# Именованные аргументы с помощью оператора ** можно объединять в словарь
# В таком случае можно задавать произвольное количество аргументов