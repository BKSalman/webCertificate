from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display

font = ImageFont.truetype('arial.ttf',30)


def reshape(something):
    reshaped_text = arabic_reshaper.reshape(something)
    bidi_text = get_display(reshaped_text)
    return bidi_text

with open('Data3.csv', 'r', encoding='UTF-8') as f:
    for i, line in enumerate(f):
        if i == 0: continue
        Position, Name, Id = line.strip().split(',')
        img = Image.open('Certificate Image 3.jpeg')
        bidi_Position = reshape(Position)
        bidi_Name = reshape(Name)
        bidi_Id = reshape(Id)
        draw = ImageDraw.Draw(img)

        xPosition, yPosition = (730, 300)
        xName, yName = (700, 300)
        xId, yId = (205, 300)

        wPosition, hPosition = draw.textsize(bidi_Position, font=font)
        wName, hName = draw.textsize(bidi_Name, font=font)
        wId, hId = draw.textsize(bidi_Id, font=font)

        draw.text(xy=(xPosition-wPosition, yPosition), text=f'{bidi_Position}', fill=(0,0,0), font=font)
        draw.text(xy=(xName-wName, yName), text=f'{bidi_Name}', fill=(0,0,0), font=font)
        draw.text(xy=(xId-wId, yId), text=f'{bidi_Id}', fill=(0,0,0), font=font)

        img_fname = f'{Name} \'s Certificate {str(i)} a.png'
        img.save(f'pictures/{img_fname}')