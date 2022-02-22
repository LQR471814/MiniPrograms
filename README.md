## ASCII Art From Image

### Make ASCII art just by inputting an image!

### Command Line Arguments

#### **Required Parameters**

```text
-i | --image-input
Path of the image you want to convert

-o | --text-output
Path of the destination of the text
```

#### **Parameters that can be set during program runtime**

```text
-ch | --char-set
Path of the character set the program will use

-pal | --palette-set
Path of the palette set the program will use
```

#### **Parameters with Defaults**

```text
-sV | --scale-vertical
The vertical scale of the image. Use -1 or leave this parameter blank for default image resolution

-sH | --scale-horizontal
The horizontal scale of the image. Use -1 or leave this parameter blank for default image resolution

-s | --global-scale
The global scale of an image. Input a percentage expressed as a decimal. (Ex. 22% = 0.22)
```

### Sets and Palettes

#### **Character Sets**

Character sets determine what characters you will use in the generated text.

```text
....................................................
....................................................
..................****##########**..................
..............**####################**..............
............**##########################**..........
..........**##########################**............
........**##########****......**####**..............
........##########**..............**................
......****######....................................
......******##**....................................
......********......................................
......******..............**##**************##**....
......******..............**##################**....
......******..............**##################**....
......******..............**##################**....
......********........................**######**....
......******##**......................**######**....
......****######**..................**########......
........##########**..............**########**......
........**##########****......****##########........
..........**##############################**........
............**##########################**..........
................**##################**..............
....................******##******..................
....................................................
....................................................
```

`HYBRID` Character set w/ `BALANCED` color palette. Scale is `0.1`

The syntax for the character set in a JSON file format is as follows:

The keys are from `b0` to `b4`. `b0` is the character symbolizing the brightest color. `b4` is the character symbolizing the darkest color.

#### Example

```JSON
{
    "b0":".",
    "b1":"~",
    "b2":"=",
    "b3":"&",
    "b4":"#"
}
```

### **Color Palettes**

Color sets define the threshold of what character to be used according to it's corresponding brightness value from the image.

```text
....................................................
........................******......................
..................####░░░░░░░░░░##**................
..............##░░░░░░░░░░░░░░░░░░░░░░**............
............##░░░░░░░░░░░░░░░░░░░░░░░░░░**..........
..........##░░░░░░░░░░░░░░░░░░░░░░░░░░##**..........
........##░░░░░░░░░░##********##░░░░##..............
......**░░░░░░░░░░**..............##**..............
......**░░░░░░░░**..................................
......****##░░##....................................
....********##**....................................
....**********............##░░░░░░░░░░░░░░░░░░##....
....**********............##░░░░░░░░░░░░░░░░░░##....
....**********............##░░░░░░░░░░░░░░░░░░##....
....**********............##░░░░░░░░░░░░░░░░░░##....
....********##**............********..##░░░░░░##....
......****##░░##......................##░░░░░░##....
......**##░░░░░░**..................##░░░░░░░░**....
......**░░░░░░░░░░##..............##░░░░░░░░##......
........##░░░░░░░░░░####******####░░░░░░░░░░**......
..........##░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░##........
............##░░░░░░░░░░░░░░░░░░░░░░░░░░##..........
..............**##░░░░░░░░░░░░░░░░░░##**............
..................**####░░░░░░####**................
....................................................
....................................................
```

`HYBRID` character set w/ `BRIGHT` color palette. Scale is `0.1`

The keys are `b0` to `b4`. `b0` is the threshold of the brightest color `b4` is the threshold of the darkest color

The way the thresholds determine the character to be used is iterating from the darkest key value and if that key value is larger than the brightness value of a pixel in the image it will insert the corresponding character to the brightness key value.

#### Example

```JSON
{
    "b0":255,
    "b1":191,
    "b2":127,
    "b3":63,
    "b4":20
}
```

From `BALENCED.json` color palette

### **Using your custom Color Palette or custom Character set**

To "install" these, you can put Color palettes in the folder named `palettes` , characters sets go in the folder named `characters`

Another method is just referencing the path of your Color palette or your Character set through command line arguments, namely the arguments `-ch / --char-set` for Character sets and `-pal / --palette-set` for Color palettes

### Experimental Color ASCII Art Generation with ANSI

#### Notes

Note: Because I cannot seem to find an ASCII art viewer I made one myself with WxPython (You probably want to use this when using experimental ANSI colored mode)

<https://github.com/LQR471814/MiniPrograms/tree/ASCII-Art-Viewer>

Note: When building with PyInstaller you should add hidden import `pkg_resources.py2_warn`

`py -m PyInstaller --hidden-import='pkg_resources.py2_warn' .\ASCIIArtByImage.py`
