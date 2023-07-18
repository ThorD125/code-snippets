import pyautogui
import cv2
import pygetwindow as gw
import keyboard
import time
import numpy as np


def wait_for_button_press(button):
    keyboard.wait(button)


wait_for_button_press('l')


def find_image_on_screen(image_path):
    while True:
        location = pyautogui.locateOnScreen(image_path, confidence=0.5)
        if location is not None:
            image_center_x = location.left + (location.width / 2)
            image_center_y = location.top + (location.height / 2)
            screen_width, screen_height = pyautogui.size()

            if (
                image_center_x >= screen_width * 0.4
                and image_center_x <= screen_width * 0.6
                and image_center_y >= screen_height * 0.4
                and image_center_y <= screen_height * 0.6
            ):
                print("Image found at the center of the screen.")
                break
            else:
                print("Moving mouse towards the image...")

                time.sleep(0.5)
                pyautogui.mouseDown()
                time.sleep(0.3)
                pyautogui.mouseUp()
                pyautogui.moveTo(image_center_x, image_center_y, duration=0.5)
        else:
            print("Image not found on the screen.")
            break


# Path to your image file
image_path = "./images/targettran.png"

# Call the function to start searching for the image
find_image_on_screen(image_path)
