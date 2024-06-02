from pynput import keyboard
import win32gui
import runFile

def on_press(key):
    if key == keyboard.Key.alt_l:
        global alt_pressed
        alt_pressed = True
    elif hasattr(key, 'char') and key.char == 'o' and alt_pressed:
        # Add your desired action here
        runFile.py_file("tkinterGUI.py")
def on_release(key):
    global alt_pressed
    if key == keyboard.Key.alt_l:
        alt_pressed = False
    elif key == keyboard.Key.esc:
        # Stop listener
        return False

# Global variable to track the state of the Alt key
alt_pressed = False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()