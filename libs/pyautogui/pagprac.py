import pyautogui as ag
import time as t
import keyboard


# Set the coordinates of the points to check
point1 = (1533, 569)
point2 = (1534, 708)
point3 = (1534, 842)
point4 = (1534, 892)

# Set the target color
target_color = (0, 118, 2)

t.sleep(2)

# Create a loop to continuosly check the pixel colors
while True:
    # Get the pixel colors at the points
    pixel1 = ag.pixel(point1[0], point1[1])
    pixel2 = ag.pixel(point1[0], point1[1])
    pixel3 = ag.pixel(point1[0], point1[1])
    pixel4 = ag.pixel(point1[0], point1[1])

    # Check if any of the pixels match the target color
    if pixel1 == target_color:
        # Click the mouse at the point
        ag.click(point1[0], point1[1])
    elif pixel2 == target_color:
        # Click the mouse at the point
        ag.click(point2[0], point2[1])
    elif pixel3 == target_color:
        # Click the mouse at the point
        ag.click(point3[0], point3[1])
    elif pixel4 == target_color:
        # Click the mouse at the point
        ag.click(point4[0], point4[1])

    # Check if the "q" key is pressed
    if keyboard.is_pressed("q"):
        break