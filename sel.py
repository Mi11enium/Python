import pyautogui
import time
import keyboard


def perform_mouse_actions():
    # Зажимаем левую кнопку мыши и перемещаем курсор
    pyautogui.mouseDown(427, 451)
    pyautogui.moveTo(1154, 845, duration=0.5)
    pyautogui.mouseUp()

    time.sleep(1)

    pyautogui.mouseDown(427, 451)
    pyautogui.moveTo(1221, 912, duration=1)
    pyautogui.mouseUp()

    pyautogui.mouseDown(427, 451)
    pyautogui.moveTo(945, 923, duration=1)
    pyautogui.mouseUp()


# Основной цикл
print("Нажмите Alt + 3 для запуска и F4 для остановки.")
while True:
    if keyboard.is_pressed('alt+3'):
        print("Start...")
        for i in range(5):
            perform_mouse_actions()
        else:
            keyboard.is_pressed('f4'):
            print("Stop.")
            break
