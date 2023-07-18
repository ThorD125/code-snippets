import pyautogui
import cv2
import pygetwindow as gw
import keyboard
import time
import numpy as np
import pyautogui
from test2 import image_path


def check_window_open(window_name):
    try:
        gw.getWindowsWithTitle(window_name)
        return True
    except gw.PyGetWindowException:
        return False


def wait_for_button_press(button):
    keyboard.wait(button)


def press(button):
    keyboard.press_and_release(button)
    time.sleep(0.3)


def pressMouse():
    time.sleep(1)
    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()


def click_image(image_path):

    time.sleep(10)

    # Load the image
    template = cv2.imread(image_path, 0)

    # Get the screen resolution
    screen_width, screen_height = pyautogui.size()

    # Take a screenshot of the screen
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to grayscale
    screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(result)

    # Calculate the middle point of the image
    image_width, image_height = template.shape[::-1]
    image_middle_x = max_loc[0] + image_width // 2
    image_middle_y = max_loc[1] + image_height // 2

    # Click the middle of the image
    click_x = image_middle_x + screen_width // 2
    click_y = image_middle_y + screen_height // 2
    pyautogui.click(click_x, click_y)


if check_window_open("Warframe"):
    warframe_window = gw.getWindowsWithTitle("Warframe")[0]
    warframe_window.activate()

    # wait_for_button_press('p')

    pressMouse()
    press('esc')
    click_image("./images/navigation.png")

    exit(0)
    # pressMouse()
    print("Navigation button found.")

    wait_for_image("./images/ukko.png")
    pressMouse()
    print("Navigation button found.")
    time.sleep(30)

    press('"')


else:
    print("Warframe window is not open.")


# Path to the target image

# Call the function to find the image on the screen and perform the click
