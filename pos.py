import pyautogui
import time

# Даем время, чтобы вы могли переместить курсор
time.sleep(5)

# Получаем текущие координаты курсора
x, y = pyautogui.position()
print(f"Координаты курсора: ({x}, {y})")
