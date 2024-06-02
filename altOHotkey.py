from pynput import keyboard as pynputKeyboard
import tkinterGUI
import keyboard


keyboard.add_hotkey('alt+o', tkinterGUI.run)
print('Listening for alt+o hotkey...')
keyboard.wait()