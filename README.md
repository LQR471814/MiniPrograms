# ASCII-Art-Viewer

An ASCII Art viewer made using WxPython

## Controls

```text
[Arrow Keys] = Pan
[-] = Zoom out
[=] = Zoom in
[o] = Open text file
[h] = Show help
[f] = Toggle full screen
[c] = Create cache for ANSI Color (Because loading may take some time)
[l] = Load cache for ANSI Color
[ESC] = Quit
```

## Experimental ANSI Color Support

The Experimental ANSI Color rendering works by taking text colored with ANSI escape sequences and converting it into two lists. One contains each character that shall be colored, and it's corresponding list contains the color value for each corresponding character.

By default, it will load the text into memory, but you can create a cache for the two lists. Therefore, if you wish to load the same image again, you do not need to go through the tedious converting of ANSI escape sequences into the two lists again.

NOTE: There is a strange bug that I can't seem to fix that causes very weird text rendering when zooming in on colored text.
