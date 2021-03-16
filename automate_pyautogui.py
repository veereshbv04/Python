# PyAutoGUI lets your Python scripts control the mouse and keyboard to automate interactions with other applications. The API is designed to be as simple. PyAutoGUI works on Windows, macOS, and Linux, and runs on Python 2 and 3.

# To install with pip, run: pip install pyautogui

# The source is available on: https://github.com/asweigart/pyautogui



import pyautogui
import time

text = " Hey ,Get up and work hard "

counter =0
while counter<0:
	pyautogui.typewrite(text)
	time.sleep(3)
	pyautogui.press('enter')
	counter += 1