# pip install pynput

from pynput.mouse import Controller, Button
import time

mouse = Controller()

# clicks every 5 minutes once
while True:
    mouse.click(Button.left, 1)
    time.sleep(150)