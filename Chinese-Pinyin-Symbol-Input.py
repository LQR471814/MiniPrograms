import keyboard
import sys

char1 = u"\u0304"
char2 = u"\u0301"
char3 = u"\u030C"
char4 = u"\u0300"
charV = u"\u0308"

charList = [char1, char2, char3, char4, charV]

helpMenu = f"""Chinese Pinyin Symbol Input v0.1.1
    [CTRL] + [ALT] + 1: First Sound
    [CTRL] + [ALT] + 2: Second Sound
    [CTRL] + [ALT] + 3: Third Sound
    [CTRL] + [ALT] + 4: Fourth Sound
    [CTRL] + [ALT] + u: The u with 2 dots above it
    [CTRL] + q: Quit
"""

def hotkeyHandler(keyType):
    global charList
    keyboard.write(charList[keyType], delay=0, restore_state_after=False)

keyboard.add_hotkey("ctrl+alt+1", hotkeyHandler, args=[0], suppress=True)
keyboard.add_hotkey("ctrl+alt+2", hotkeyHandler, args=[1], suppress=True)
keyboard.add_hotkey("ctrl+alt+3", hotkeyHandler, args=[2], suppress=True)
keyboard.add_hotkey("ctrl+alt+4", hotkeyHandler, args=[3], suppress=True)
keyboard.add_hotkey("ctrl+alt+u", hotkeyHandler, args=[4], suppress=True)
keyboard.add_hotkey("ctrl+q", sys.exit, args=[0], suppress=True)

print(helpMenu)

while True:
    pass