import pyautogui
import time
import keyboard

def send_message():
    message = input("Text:")
    amount = 400
    time.sleep(6)

    for i in range(amount):
        pass

    while amount > 0:
        if keyboard.is_pressed("esc"):
            break
        else:
            amount -= 1

            pyautogui.typewrite(message.strip())
            pyautogui.press("enter")


send_message()
