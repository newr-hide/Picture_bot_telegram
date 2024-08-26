from PIL import ImageFont
import os

font_path_lobster = os.path.join(os.path.dirname("file"), 'fonst', 'Lobster-Regular.ttf') #Строка указывающая где шрифт
font_lobster = ImageFont.truetype(font_path_lobster, size=100)


font_path_rosarium = os.path.join(os.path.dirname("file"), 'fonst', 'Rosarium.ttf') #Строка указывающая где шрифт
font_rosarium = ImageFont.truetype(font_path_rosarium, size=100)

font_path_majestik = os.path.join(os.path.dirname("file"), 'fonst', 'Majestic_0.ttf') #Строка указывающая где шрифт
font_majestic = ImageFont.truetype(font_path_majestik, size=100)