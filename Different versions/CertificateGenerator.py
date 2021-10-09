from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display

font = ImageFont.truetype('arial.ttf',30)


def reshape(something):
    reshaped_text = arabic_reshaper.reshape(something)
    bidi_text = get_display(reshaped_text)
    return bidi_text

with open('Data.csv', 'r', encoding='UTF-8') as f:
    for i, line in enumerate(f):
        if i == 0: continue
        Name, Age = line.strip().split(',')
        img = Image.open('samples/Certificate Image.jpg')
        bidi_Name = reshape(Name)
        bidi_Age = reshape(Age)
        draw = ImageDraw.Draw(img)
        x, y = (600, 427)
        x2, y2 = (600, 600)
        w, h = draw.textsize(bidi_Name, font=font)
        w2, h2 = draw.textsize(bidi_Age, font=font)
        draw.text(xy=(x-w, y), text=f'{bidi_Name}', fill=(0,0,0), font=font)
        draw.text(xy=(x2-w2, y2), text=f'{bidi_Age}', fill=(0,0,0), font=font)
        img_fname = f'{Name} \'s Certificate {str(i)}.png'
        img.save(f'pictures/{img_fname}')