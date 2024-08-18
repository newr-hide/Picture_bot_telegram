from PIL import Image, ImageFont, ImageDraw
import os

font_path = os.path.join(os.path.dirname("file"), 'fonts', 'Lobster-Regular.ttf') #Строка указывающая где шрифт
font = ImageFont.truetype(font_path, size=16)


draw = ImageDraw.Draw('image')
draw.text((110, 22), "Hello, World!", (0, 0, 0), font=font)