from pynput import keyboard
import sys

current = set()
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.Key.esc},
    {keyboard.Key.ctrl_l, keyboard.Key.alt_l, keyboard.KeyCode(char="1")}
]
blacklist = ["\x01", "\x02", "\x03", "\x04", "\x05", "\x06", "\x07", "\x08", "\x09", "\x10", "\x11", "\x12", "\x13", "\x14", "\x15", "\x16", "\x17", "\x18", "\x19", "\x20", "\x21", "\x22", "\x23", "\x24"]

def on_press(key):
    print("-----------------------")
    try:
        print(key)
    except:
        pass
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        print(current)

        for COMBO in COMBINATIONS:
            allPressed = True
            for k in COMBO:
                if k not in current:
                    allPressed = False
                    break
            if allPressed == True:
                execute(COMBO)
                break
            else:
                return

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        try:
            current.remove(key)
        except:
            pass

def execute(keyCombination):
    if keyCombination == COMBINATIONS[0]: #? On quit combination
        sys.exit(0)
    elif keyCombination == COMBINATIONS[1]: #? On first sound
        print("yup")

def isCtrl(key):
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        return True
    return False

def isAlt(key):
    if key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
        return True
    return False

def hotkeyHandler(keyType):
    global charList
    keyboard.write(charList[keyType], delay=0, restore_state_after=False)

def main():
    # keyboard = Controller()

    char1 = u"\u0304"
    char2 = u"\u0301"
    char3 = u"\u030C"
    char4 = u"\u0300"
    charV = u"\u0308"

    charList = [char1, char2, char3, char4, charV]

    # keyboard.add_hotkey("ctrl+alt+1", hotkeyHandler, args=[0], suppress=True)
    # keyboard.add_hotkey("ctrl+alt+2", hotkeyHandler, args=[1], suppress=True)
    # keyboard.add_hotkey("ctrl+alt+3", hotkeyHandler, args=[2], suppress=True)
    # keyboard.add_hotkey("ctrl+alt+4", hotkeyHandler, args=[3], suppress=True)
    # keyboard.add_hotkey("ctrl+alt+u", hotkeyHandler, args=[4], suppress=True)
    # keyboard.add_hotkey("ctrl+q", sys.exit, args=[0], suppress=True)

    helpMenu = f"""Chinese Pinyin Symbol Input v0.2.0
        [CTRL] + [ALT] + 1: First Sound
        [CTRL] + [ALT] + 2: Second Sound
        [CTRL] + [ALT] + 3: Third Sound
        [CTRL] + [ALT] + 4: Fourth Sound
        [CTRL] + [ALT] + u: The u with 2 dots above it
        [SHIFT] + [ESC] : Quit
    """

    print(helpMenu)
    
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()