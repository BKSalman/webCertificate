import os
import smtplib
import imghdr
from email.message import EmailMessage
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
import sqlite3
import threading
from threading import Thread, Lock

import time

font = ImageFont.truetype('arial.ttf'),30
lock = threading.Lock()


EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

def reshape(something):
    reshaped_text = arabic_reshaper.reshape(something)
    bidi_text = get_display(reshaped_text)
    return bidi_text

def generateCertificate(pre, id, name):
    Pre = pre
    Id = id
    Name = name
    img = Image.open('samples/Certificate Image 3.jpg')
    bidi_Pre = reshape(Pre)
    bidi_Name = reshape(Name)
    draw = ImageDraw.Draw(img)

    xPosition, yPosition = (730, 300)
    xName, yName = (700, 300)
    xId, yId = (205, 300)

    wPosition, _ = draw.textsize(bidi_Pre, font=font)
    wName, _ = draw.textsize(bidi_Name, font=font)
    wId, _ = draw.textsize(Id, font=font)

    draw.text(xy=(xPosition-wPosition, yPosition), text=f'{bidi_Pre}', fill=(0,0,0), font=font)
    draw.text(xy=(xName-wName, yName), text=f'{bidi_Name}', fill=(0,0,0), font=font)
    draw.text(xy=(xId-wId, yId), text=f'{Id}', fill=(0,0,0), font=font)

    img_fname = f'Certificate {Id}.png'
    img.save(f'/webApp/webCertificate/media/{img_fname}')


def sendEmail(name, email, id):
    Name = name
    Email = email
    Id = id

    img_fname = f'Certificate {Id}.png'
    msg = EmailMessage()
    msg['Subject'] = f'شهادة {Name}'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = Email
    msg.set_content('')

    with open(f'/webApp/webCertificate/media//{img_fname}', 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)