# ASCII Art From Image

### Make ASCII art just by inputting an image!

## Command Line Arguments

### **Required Parameters**

#### `-i | --image-input Ex. /path/to/your/image.png`

Input the path to the image you want to convert

#### `-o | --text-output Ex. /destination/path/output.txt`

Input the path to the destination of the text

### **Parameters with Choice during program runtime**

#### `-ch | --char-set Ex. /path/to/your/character_set.json`

Input the path of the character set the program will use.

#### `-pal | --palette-set Ex. /path/to/your/palette_set.json`

Input the path of the palette set the program will use

### **Parameters with Defaults**

#### `-sV | --scale-vertical Ex. 1280`

Input the vertical scale of the image. This will stretch the image. Input -1 or leave this parameter blank for default image resolution

#### `-sV | --scale-vertical Ex. 720`

Input the horizontal scale of the image. This will stretch the image. Input -1 or leave this parameter blank for default image resolution

#### `-s | --global-scale Ex. 0.22`

Input the global scale of an image. This will scale the image on both sides, vertical and horizontal, you should input a percentage expressed as a decimal. (Ex. 22% = 0.22)

## Sets and Palettes

### **Character Sets**

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

The keys are from "b0" to "b4"

b0 is the character symbolizing the brightest color.

b4 is the character symbolizing the darkest color.

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

The syntax of the color set is as follows:

The keys are "b0" to "b4"

b0 is the threshold of the brightest color

b4 is the threshold of the darkest color

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

## Experimental Color ASCII Art Generation with ANSI

### Notes

Note: An External library used to do ANSI coloring

<https://pypi.org/project/Colr/>

Note 2: Because I cannot seem to find an ASCII art viewer I made one myself with WxPython (You probably want to use this when using experimental ANSI colored mode)

<https://github.com/LQR471814/MiniPrograms/tree/ASCII-Art-Viewer>

### Command Line Arguments

### **Required Parameters**

#### `-i | --image-input Ex. /path/to/your/image.png`

Input the path to the image you want to convert

#### `-o | --text-output Ex. /destination/path/output.txt`

Input the path to the destination of the text

#### `-c | --char Ex. #`

The character that will be used for all brightness values although it will be colored according to each pixel.

### **Parameters with Defaults**

#### `-sV | --scale-vertical Ex. 1280`

Input the vertical scale of the image. This will stretch the image. Input -1 or leave this parameter blank for default image resolution

#### `-sV | --scale-vertical Ex. 720`

Input the horizontal scale of the image. This will stretch the image. Input -1 or leave this parameter blank for default image resolution

#### `-s | --global-scale Ex. 0.22`

Input the global scale of an image. This will scale the image on both sides, vertical and horizontal, you should input a percentage expressed as a decimal. (Ex. 22% = 0.22)
