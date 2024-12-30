import threading
import time
from pynput.mouse import Controller, Button, Listener
from pynput.keyboard import Key, Listener as KeyboardListener

# Initialize mouse controller
mouse = Controller()

# Autoclicker settings
clicking = False  # Toggled state of the autoclicker
click_delay = 0.001  # Delay between clicks in seconds (1 millisecond)

# Define the side mouse buttons (you might need to adjust based on your mouse)
SIDE_BUTTON_1 = Button.x1  # Back button
SIDE_BUTTON_2 = Button.x2  # Forward button

def autoclicker():
    global clicking
    while True:
        if clicking:
            mouse.click(Button.left)
        time.sleep(click_delay)

def toggle_clicker(button):
    global clicking
    if button == SIDE_BUTTON_1:  # Start/Stop toggling on side button 1
        clicking = not clicking

def on_click(x, y, button, pressed):
    if pressed:
        toggle_clicker(button)

# Start the autoclicker in a separate thread
thread = threading.Thread(target=autoclicker, daemon=True)
thread.start()

# Listen for mouse events
with Listener(on_click=on_click) as listener:
    listener.join()
