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

res1680x1050 = {
    'start': [(270, 470), '0, 172, 134'],  # start
    'car not found': [(1150, 530), '255, 255, 255'],  # car not found
    'car found': [(751, 380), '152, 152, 152'],  # car found
    'car sold': [(343, 410), '115, 115, 115'],  # car sold
}

res1920x1080 = {
    'start': [(302, 473), '0, 181, 146'],  # start
    'car not found': [(1209, 566), '255, 255, 255'],  # car not found
    'car found': [(858, 374), '195, 195, 195'],  # car found
    'car sold': [(404, 406), '150, 150, 150'],  # car sold
}

pixels = res1920x1080
# pixels = res1680x1050

while True:
    while (True):
        pixelColor = pyautogui.screenshot().getpixel(pixels.get('start')[0])  # start

        if (f'{pixelColor[0]}, {pixelColor[1]}, {pixelColor[2]}' == pixels.get('start')[1]): break
        time.sleep(0.5)

    controller.press(Key.enter)
    controller.release(Key.enter)

    time.sleep(0.5)

    controller.press(Key.enter)
    controller.release(Key.enter)

    time.sleep(0.5)

    while (True):
        pixelColor = pyautogui.screenshot().getpixel(pixels.get('car not found')[0])  # car not found

        if (f'{pixelColor[0]}, {pixelColor[1]}, {pixelColor[2]}' == pixels.get('car not found')[1]):
            controller.press(Key.esc)
            controller.release(Key.esc)
            break

        pixelColor = pyautogui.screenshot().getpixel(pixels.get('car found')[0])  # car found
        if (f'{pixelColor[0]}, {pixelColor[1]}, {pixelColor[2]}' == pixels.get('car found')[1]):
            pixelColor = pyautogui.screenshot().getpixel(pixels.get('car sold')[0])  # car sold
            if (f'{pixelColor[0]}, {pixelColor[1]}, {pixelColor[2]}' == pixels.get('car sold')[1]):
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

            time.sleep(1)

            controller.press(Key.esc)
            controller.release(Key.esc)

            time.sleep(1)

            controller.press(Key.esc)
            controller.release(Key.esc)
            break

        time.sleep(0.5)
