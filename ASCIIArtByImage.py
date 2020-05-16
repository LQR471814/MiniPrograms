import argparse
import json
import os
from os import listdir
from os.path import isfile, join

from PIL import Image


def sortDictionaryAscending(inpDict):
    result = {}
    sortedList = sorted(inpDict)
    for key in sortedList:
        result[key] = inpDict[key]
    return result

def printChoices(choices):
    msg = ""
    for choice, i in zip(choices, range(len(choices))):
        if i == len(choices) - 1:
            msg += choice
        else:
            msg += choice + " | "
    return msg

parser = argparse.ArgumentParser(description='ASCII Art from Image v0.1.0')

#? Required
parser.add_argument("-i", "--image-input", required=True, help="Ex. /path/to/your/image.png")
parser.add_argument("-o", "--text-output", required=True, help="Ex. /destination/path/output.txt")

#? User choice in program later
parser.add_argument("-ch", "--char-set", help="Ex. /path/to/your/character_set.json")
parser.add_argument("-pal", "--palette-set", help="Ex. /path/to/your/palette_set.json")

#? Has Defaults
parser.add_argument("-sV", "--scale-vertical", default=-1, help="Ex. 1280")
parser.add_argument("-sH", "--scale-horizontal", default=-1, help="Ex. 720")
parser.add_argument("-s", "--global-scale", default=1, help="Ex. 0.22")
parser.add_argument("-rV", "--stretch-vertical", default=1, help="Ex. 1")
parser.add_argument("-rH", "--stretch-horizontal", default=2, help="Ex. 2")
args = parser.parse_args()

srcDir = os.path.dirname(os.path.abspath(__file__)) + "\\"

if args.char_set == None:
    characterSets = [f for f in listdir(srcDir + "characters\\") if isfile(join(srcDir + "characters\\", f))]
    for file, i in zip(characterSets, range(len(characterSets))):
        characterSets[i] = file.replace(".json", "")
    print("Pick a character set!")
    print(printChoices(characterSets))

    characterSetFilename = input(" > ")
    f = open(srcDir + "characters\\" + characterSetFilename + ".json", "r")
    charData = json.loads(f.read())
    b0 = charData["b0"]
    b1 = charData["b1"]
    b2 = charData["b2"]
    b3 = charData["b3"]
    b4 = charData["b4"]
    f.close()
else:
    f = open(args.char_set, "r")
    charData = json.loads(f.read())
    b0 = charData["b0"]
    b1 = charData["b1"]
    b2 = charData["b2"]
    b3 = charData["b3"]
    b4 = charData["b4"]
    f.close()

if args.palette_set == None:
    paletteSets = [f for f in listdir(srcDir + "palettes\\") if isfile(join(srcDir + "palettes\\", f))]
    for file, i in zip(paletteSets, range(len(paletteSets))):
        paletteSets[i] = file.replace(".json", "")
    print("Pick a palette set!")
    print(printChoices(paletteSets))

    paletteSetFilename = input(" > ")
    f = open(srcDir + "palettes\\" + paletteSetFilename + ".json", "r")
    keys = json.loads(f.read())

    paletteData = {}
    paletteData[keys["b0"]] = b0
    paletteData[keys["b1"]] = b1
    paletteData[keys["b2"]] = b2
    paletteData[keys["b3"]] = b3
    paletteData[keys["b4"]] = b4
    paletteData = sortDictionaryAscending(paletteData)
else:
    f = open(args.palette_set, "r")
    keys = json.loads(f.read())

    paletteData = {}
    paletteData[keys["b0"]] = b0
    paletteData[keys["b1"]] = b1
    paletteData[keys["b2"]] = b2
    paletteData[keys["b3"]] = b3
    paletteData[keys["b4"]] = b4
    paletteData = sortDictionaryAscending(paletteData)

#? CHARACTER SETS:

print("Character Set: " + "0: " + b0 + ", 1: " + b1 + ", 2: " + b2 + ", 3: " + b3 + ", 4: " + b4)

imageDimension = [int(args.scale_horizontal), int(args.scale_vertical)]
scale = float(args.global_scale)
stretchH = int(args.stretch_horizontal)
stretchV = int(args.stretch_vertical)

im = Image.open(args.image_input, "r").convert("LA") #? Image path goes here!

#? CODE

width, height = im.size
if imageDimension[0] == -1:
    imageDimension[0] = width
else:
    width = imageDimension[0]

if imageDimension[1] == -1:
    imageDimension[1] = height
else:
    height = imageDimension[1]

imageDimension[0] = int(round(imageDimension[0] * scale, 0))
imageDimension[1] = int(round(imageDimension[1] * scale, 0))
width = imageDimension[0]
height = imageDimension[1]

print("Dimensions: " + str(imageDimension[0]) + "x" + str(imageDimension[1]))
print(paletteData)

im = im.resize(imageDimension)

linedImage = []
for y in range(height):
    tmp = []
    for x in range(width):
        tmp.append(im.getpixel((x, y))[0])
    linedImage.append(tmp)

result = ""
for line in linedImage:
    for i in range(stretchV):
        for pixel in line:
            for value in paletteData:
                if pixel <= value:
                    for i in range(stretchH):
                        result += paletteData[value]
                    break
        result += "\n"

outputObj = open(args.text_output, mode="w", encoding="utf-8")
outputObj.write(result)
