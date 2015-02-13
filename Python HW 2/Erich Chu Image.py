#Erich Chu
import random
import string
from PIL import Image
from PIL import ImageDraw,ImageFont

name = raw_input("What is your name?")
letter = name[:1]
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
img = Image.new("RGB", (200,200), (0,0,0))
draw = ImageDraw.Draw(img)
draw.rectangle((0, 0, 200, 200), fill=(r,g,b))
font = ImageFont.truetype("arial.ttf",50)
draw.text((88,72), letter, (255,255,255), font=font)
img.show()
