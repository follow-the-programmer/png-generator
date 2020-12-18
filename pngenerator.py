from PIL import Image
from random import randint, choice
width = int(input("image width in pixels: "))
height = int(input("image height in pixels: "))
im = Image.new('RGBA', (height, width))

i = 0
j = 0

def gradient(image_size, iterator):
    return int(iterator // (image_size / 255))


print("red\n(gl for gradient per line;\n gc for gradient per column;\n(number from 0 to 255): static value;\n(two numbers from 0-255 separed by a "
      "space): random values between those two)\n choose one of them ")

redi = input().split()

print("green\n(gl for gradient per line;\n gc for gradient per column;\n(number from 0 to 255): static value;\n(two numbers from 0-255 separed by a "
      "space): random values between those two)\n choose one of them ")

greeni = input().split()

print("blue\n(gl for gradient per line;\n gc for gradient per column;\n(number from 0 to 255): static value;\n(two numbers from 0-255 separed by a "
      "space): random values between those two)\n choose one of them ")

bluei = input().split()


def know(redi):
    if redi[0] == "gl":
        return gradient(width, j)
    elif redi[0] == "gc":
        return gradient(height, i)
    elif redi[0] == "gd":
        return gradient((height + width) // 2, choice([i ^ j, i | j]))
    elif len(redi) == 2 and (redi[0].isdigit() and redi[1].isdigit()):
        return randint(int(redi[0]), int(redi[1]))
    elif redi[0].isdigit():
        return int(redi[0])

for i in range(height):
    for j in range(width):
        red = know(redi)
        green = know(greeni)
        blue = know(bluei)
        im.putpixel((i, j), (red, green, blue, 255))

im.save("image5.png")