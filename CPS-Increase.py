import mouse
import keyboard

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
    quit()

mouse.on_click(onLeft)
mouse.on_right_click(onRight)

keyboard.add_hotkey("alt+f", toggle, suppress=True)
keyboard.add_hotkey("alt+q", onQuit, suppress=True)

while True:
    pass