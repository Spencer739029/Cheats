import pyautogui
import threading
import time

# Coordinates for main click area and capybara button
x_y = 733, 347
capybara = 347, 402

# Target color for main click area
target_colour = (245, 245, 245)

def ascension():
    # Perform ascension sequence by clicking specific coordinates
    pyautogui.moveTo(737, 498)
    pyautogui.click(button="left")
    time.sleep(0.5)
    pyautogui.moveTo(410, 466)
    pyautogui.click(button="left")
    return

try:
    while True:
        # Get current color at main click area
        current_colour = pyautogui.pixel(733, 347)

        # Check for special popup or event by pixel colors at specific locations
        if pyautogui.pixel(275, 355) == (255, 255, 255) and pyautogui.pixel(412, 281) == (36, 140, 207) and pyautogui.pixel(432, 481) == (245, 245, 245):
            pyautogui.moveTo(432, 481)
            pyautogui.click(button="left")
            time.sleep(3)
            # Scroll down to reveal more content
            for i in range(100):
                pyautogui.scroll(2000)
            continue

        # Check if ascension is available by pixel color
        if pyautogui.pixel(737, 498) == (245, 245, 245):
            # Schedule ascension after 5 minutes, only if not already scheduled
            if not hasattr(threading, "ascension_scheduled") or not threading.ascension_scheduled:
                threading.ascension_scheduled = True
                def ascension_wrapper():
                    ascension()
                    threading.ascension_scheduled = False
                threading.Timer(300, ascension_wrapper).start()

        # Main click logic based on color
        if current_colour == target_colour:
            pyautogui.moveTo(x_y)
            pyautogui.click(button="left")
            pyautogui.moveTo(capybara)
        # Handle alternate color states
        elif (current_colour == (147, 147, 147) and current_colour != (108, 170, 181)) or current_colour == (94, 141, 149) or current_colour == (107, 136, 141) or current_colour == (122, 173, 181):
            pyautogui.moveTo(x_y)
            pyautogui.click(button="left")
            for i in range(50):
                pyautogui.scroll(5000)
        else:
            # Default action if no color matches
            pyautogui.moveTo(x_y)
            pyautogui.scroll(-1000)
            pyautogui.moveTo(capybara)
            pyautogui.click(button="left")

except KeyboardInterrupt:
    print("\nStopped.")