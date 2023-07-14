import pyautogui
import cv2
import pygetwindow as gw
import keyboard
import time
import numpy as np


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


def find_image_on_screen(image_path):
    # Load the target image
    time.sleep(5)

    target_image = cv2.imread(image_path)

    # Get the screen dimensions
    screen_width, screen_height = pyautogui.size()

    # Take a screenshot of the screen
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to an OpenCV image
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Use OpenCV template matching to find the image on the screen
    result = cv2.matchTemplate(screenshot, target_image, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # If the image is found on the screen
    if max_val > 0.8:
        # Calculate the center of the image
        image_width = target_image.shape[1]
        image_height = target_image.shape[0]
        center_x = max_loc[0] + (image_width // 2)
        center_y = max_loc[1] + (image_height // 2)

        # Move the cursor to the center of the image
        pyautogui.moveTo(center_x, center_y, 0.89)

    else:
        print("Image not found on the screen.")
        exit()


if check_window_open("Warframe"):
    warframe_window = gw.getWindowsWithTitle("Warframe")[0]
    warframe_window.activate()

    # wait_for_button_press('p')

    pressMouse()
    press('esc')
    find_image_on_screen("./images/navigation.png")
    pressMouse()
    print("Navigation button found.")

    find_image_on_screen("./images/ukko.png")
    pressMouse()
    print("Navigation button found.")
    time.sleep(30)

    press('"')


else:
    print("Warframe window is not open.")


# Path to the target image

# Call the function to find the image on the screen and perform the click
