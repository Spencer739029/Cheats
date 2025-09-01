# Finish later
import pyautogui
import threading
import time

def nextmap():
    pyautogui.moveTo(772, 435)
    pyautogui.click(button="left")
    return

while True:
    pyautogui.moveTo(620, 389)
    pyautogui.click(button="left")
    if pyautogui.pixel(129, 568) == (123, 123, 123) and pyautogui.pixel(264, 583) == (53, 253, 255):
        time.sleep(10)
        pyautogui.moveTo(765, 508)
        time.sleep(0.15)
        pyautogui.click(button="left")

    if pyautogui.pixel(422, 462) == (28, 233, 248):
        pyautogui.moveTo(422, 462)
        time.sleep(0.15)
        pyautogui.click(button="left")

    if pyautogui.pixel(482, 483) == (20, 221, 93):
        pyautogui.moveTo(482, 483)
        time.sleep(0.15)
        pyautogui.click(button="left")

    if pyautogui.pixel(539, 482) == (255, 177, 24):
        pyautogui.moveTo(539, 482)
        time.sleep(0.15)
        pyautogui.click(button="left")

    if pyautogui.pixel(452, 415) == (203, 94, 255):
        pyautogui.moveTo(452, 415)
        time.sleep(0.15)
        pyautogui.click(button="left")

    if pyautogui.pixel(348, 484) == (158, 161, 162):
        pyautogui.moveTo(348, 484)
        time.sleep(0.15)
        pyautogui.click(button="left")

    if pyautogui.pixel(772, 435) == (105, 115, 163):
        pyautogui.moveTo(772, 435)
        time.sleep(0.15)
        threading.Timer(100, nextmap).start()

    if pyautogui.pixel(521, 282) == (255, 84, 84):
        pyautogui.moveTo(521, 282)
        time.sleep(0.15)
        pyautogui.moveTo(521, 282)
        pyautogui.click(button="left")
