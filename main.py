import pyautogui
import time


def send_message():
    message = input("Text:")
    amount = 100
    time.sleep(6)

    for i in range(amount):
        pass

    while amount > 0:
        amount -= 1

        pyautogui.typewrite(message.strip())
        pyautogui.press("enter")


send_message()
