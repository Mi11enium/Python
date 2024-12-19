import pyautogui
pg = pyautogui

# Путь к файлу изображения, которое нужно найти
img_path = 'D:\Learn\Courses\Python\libs\cup.png'

# Поиск изображения на экране
loc = pg.locateOnScreen(img_path)

if loc:
    print(f"Изображение найдено на позиции: {loc}")
    # Клик по центру найденного изображения
    pg.click(pg.center(loc))
else:
    print("Изображение не найдено.")