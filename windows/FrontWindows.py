import pygetwindow as gw
import pyautogui
import time
import pyperclip

class FrontWindows:

    def __init__(self):
        pass
    
    def input_text_in_active_window(self, text):
        # Get the active window
        active_window = gw.getActiveWindow()

        if active_window:
            # Activate the window
            active_window.activate()
            # copying the text to clipboard
            pyperclip.copy(text)
            # Type the text using pyautogui
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)  # You might need to adjust this delay based on the application's responsiveness
        else:
            print("No active window found.")
