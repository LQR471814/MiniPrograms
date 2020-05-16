from colr import color
import subprocess
import os

f = open("ANSI.txt", "w")
x = color("A", fore=(255, 0, 0)) + color("A", fore=(0, 255, 0)) + color("A", fore=(0, 0, 255))
y = color("B", fore=(255, 0, 0)) + color("B", fore=(0, 255, 0)) + color("B", fore=(0, 0, 255))
print(x + "\n" + y)

rgb = []
characters = []
ls = (x + "\n" + y).split(chr(27) + "[")
for thing, i in zip(ls, range(len(ls))):
    if thing == "":
        ls.pop(i)
    if thing == "0m":
        ls.pop(i)
for value, i in zip(ls, range(len(ls))):
    if "\n" in value:
        rgb.append("\n")
        characters.append("\n")
        continue
    rgb.append([])
    print(value)
    value = value.replace("38;2;", "")
    value = value.split(";")
    characters.append(value[2][-1])
    rgb[i].append(value[0])
    rgb[i].append(value[1])
    rgb[i].append(value[2][0:-1].replace("m", ""))
    ls[i] = value
f.write(str(ls) + "\n" + str(rgb) + "\n" + str(characters))
f.close()

a = subprocess.check_output(os.getcwd() + "\\ANSI.txt", shell=True)