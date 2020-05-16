import argparse

from colr import color
from PIL import Image

parser = argparse.ArgumentParser(description='Experimental ASCII Art from Image Colored v0.1.0')

#? Required

parser.add_argument("-i", "--image-input", required=True, help="Ex. /path/to/your/image.png")
parser.add_argument("-o", "--text-output", required=True, help="Ex. /destination/path/output.txt")
parser.add_argument("-c", "--char", required=True, help="Ex. #")

#? With Defaults

parser.add_argument("-sV", "--scale-vertical", default=-1, help="Ex. 1280")
parser.add_argument("-sH", "--scale-horizontal", default=-1, help="Ex. 720")
parser.add_argument("-s", "--global-scale", default=1, help="Ex. 0.22")

args = parser.parse_args()

imageDimension = [int(args.scale_horizontal), int(args.scale_vertical)]
scale = float(args.global_scale)

im = Image.open(args.image_input, "r")

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

output = ""
for y in range(height):
    for x in range(width):
        output += color(args.char, fore=im.getpixel((x, y)))
    output += "\n"

f = open(args.text_output, "w", encoding="utf-8")
f.write(output)
