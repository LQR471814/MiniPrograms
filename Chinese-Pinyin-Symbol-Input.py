import keyboard
import sys

char1 = u"\u0304"
char2 = u"\u0301"
char3 = u"\u030C"
char4 = u"\u0300"
charV = u"\u0308"

helpMenu = f"""Chinese Pinyin Symbol Input v0.1.0
    [ALT] + 1: {char1}
    [ALT] + 2: {char2}
    [ALT] + 3: {char3}
    [ALT] + 4: {char4}
    [ALT] + v: {charV}
    [CTRL] + q: Quit
"""

charList = [char1, char2, char3, char4, charV]

def hotkeyHandler(keyType):
    global charList
    keyboard.write(charList[keyType], delay=0, restore_state_after=False)

keyboard.add_hotkey("alt+1", hotkeyHandler, args=[0], suppress=True)
keyboard.add_hotkey("alt+2", hotkeyHandler, args=[1], suppress=True)
keyboard.add_hotkey("alt+3", hotkeyHandler, args=[2], suppress=True)
keyboard.add_hotkey("alt+4", hotkeyHandler, args=[3], suppress=True)
keyboard.add_hotkey("alt+v", hotkeyHandler, args=[4], suppress=True)
keyboard.add_hotkey("ctrl+q", sys.exit, args=[0], suppress=True)

print(helpMenu)

while True:
    pass