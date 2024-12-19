# Аргументы с ключевыми словами
# Использование аргументов с ключевыми словами делает код более читабельным
def get_posts_info(name, posts_qty):
    info = f"{name} wrote {posts_qty} posts"
    return info

info = get_posts_info(posts_qty=30, name='Bogdan')  # Аргументы с ключевыми словами. Порядок аргументов НЕ ВАЖЕН
print(info)