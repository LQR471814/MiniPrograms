import mouse
import keyboard
import sys

toggled = -1
x = 0
y = 0
thresh = 1

def onLeft():
    global x
    global thresh
    global toggled

    if toggled > 0:
        if x > thresh:
            x = 0
            mouse.click("left")
            return
        x += 1

def onRight():
    global y
    global thresh
    global toggled

    if toggled > 0:
        if y > thresh:
            y = 0
            mouse.click("right")
            return
        y += 1

def toggle():
    global toggled

    toggled *= -1

def onQuit():
    mouse.unhook_all()
    keyboard.unhook_all()
    sys.exit(0)

mouse.on_click(onLeft)
mouse.on_right_click(onRight)

keyboard.add_hotkey("alt+f", toggle, suppress=True)
keyboard.add_hotkey("alt+q", onQuit, suppress=True)

while True:
    pass