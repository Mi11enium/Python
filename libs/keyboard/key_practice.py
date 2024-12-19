from pyautogui import click
import time as t
import sys
import keyboard


def close_hotkeys():
    sys.exit(0)

def clicker():
    click(clicks=5)

def click_power1():
    click(clicks=50)

def click_power2():
    click(clicks=500)

def click_power3():
    click(clicks=1000)

def writeof():
    print('Hello')

keyboard.add_hotkey('ctrl', close_hotkeys)
keyboard.add_hotkey('alt', clicker)
keyboard.add_hotkey('z', click_power1)
keyboard.add_hotkey('x', click_power2)
keyboard.add_hotkey('c', click_power3)

while True:
    pass
