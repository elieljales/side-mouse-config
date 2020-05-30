from pynput import mouse
from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard
from pyautogui import hotkey
import time

initial_time = time.time()

def on_click(x, y, button, pressed):
    global initial_time
    passed_time = time.time()
    if((passed_time - initial_time) >= 0.6):
        initial_time = time.time()
        keyboard = Controller()
        if button == mouse.Button.button8:
           hotkey('winleft', 'h')    

with mouse.Listener(on_click=on_click) as listener:
        listener.join()
