
import pyautogui as ag
import time as t

# Поиск картинки, перемещение и клик в её центр
"""
t.sleep(1)

x, y = ag.locateCenterOnScreen('D:\Learn\Courses\Python\libs\pyautogui\\five.png', confidence=0.8)

ag.moveTo(x, y, duration=1)
ag.click()
"""
# Определение цвета RGB по координатам

x, y = ag.position()
rgbcolor = ag.pixel(x, y)
print(rgbcolor)  # (0, 118, 2)