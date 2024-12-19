import pyautogui as ag
import time as t
import keyboard


# Путь к файлу изображения, которое нужно найти
template = ag.locateOnScreen('D:\Learn\Courses\Python\libs\pyautogui\\but2.png', confidence=0.8)
region = ag.Region(1100, 1600, 500, 600)
all_buttons = ag.locateAll(template, region=region)


t.sleep(2)

# Create a loop to continuosly check the pixel colors
# Вывод координат всех найденных вхождений
for button in all_buttons:
    print(f"Найдено вхождение: Лево {button.left}, Верх {button.top}")
