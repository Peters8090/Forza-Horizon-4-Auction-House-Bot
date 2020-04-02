import time

import pyautogui
from pynput.keyboard import Key, Controller, Listener

controller = Controller()

arr = []

time.sleep(2)


def on_press(key):
    if hasattr(key, 'char'):
        arr.insert(0, key.char)


l = Listener(on_press=on_press)

l.start()

while True:
    while (True):
        pixelColor = pyautogui.screenshot().getpixel((302, 473))  # start

        if (f'{pixelColor[0]}, {pixelColor[1]}, {pixelColor[2]}' == '0, 181, 146'): break
        time.sleep(0.5)

    controller.press(Key.enter)
    controller.release(Key.enter)

    time.sleep(0.75)

    controller.press(Key.enter)
    controller.release(Key.enter)

    time.sleep(0.5)

    while (True):
        pixelColor = pyautogui.screenshot().getpixel((1209, 566))  # car not found

        if (f'{pixelColor[0]}, {pixelColor[1]}, {pixelColor[2]}' == '255, 255, 255'):
            controller.press(Key.esc)
            controller.release(Key.esc)
            break

        pixelColor = pyautogui.screenshot().getpixel((858, 374))  # car found
        if (f'{pixelColor[0]}, {pixelColor[1]}, {pixelColor[2]}' == '195, 195, 195'):
            pixelColor = pyautogui.screenshot().getpixel((404, 406))  # car sold
            if (f'{pixelColor[0]}, {pixelColor[1]}, {pixelColor[2]}' == '150, 150, 150'):
                controller.press(Key.esc)
                controller.release(Key.esc)

            controller.press('y')
            controller.release('y')

            time.sleep(0.3)

            controller.press(Key.down)
            controller.release(Key.down)

            time.sleep(0.3)

            controller.press(Key.enter)
            controller.release(Key.enter)

            time.sleep(0.3)

            controller.press(Key.enter)
            controller.release(Key.enter)  # bought

            time.sleep(6)

            controller.press(Key.enter)
            controller.release(Key.enter)

            time.sleep(0.5)

            controller.press(Key.esc)
            controller.release(Key.esc)

            time.sleep(0.5)

            controller.press(Key.esc)
            controller.release(Key.esc)
            break

        time.sleep(0.5)
