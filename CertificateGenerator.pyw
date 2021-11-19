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

font = ImageFont.truetype('arial.ttf',30)
lock = threading.Lock()

connection = sqlite3.connect("Data.sqlite", check_same_thread=False)
cur = connection.cursor()

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

def reshape(something):
    reshaped_text = arabic_reshaper.reshape(something)
    bidi_text = get_display(reshaped_text)
    return bidi_text

def generateCertificate(row, n):
    Pre = row[0]
    Id = row[1]
    Name = row[2]
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

    img_fname = f'Certificate{n}.png'
    img.save(f'pictures/{img_fname}')

def threadedCertificate():
    n = 0
    threads = []
    start = time.perf_counter()
    sqlquery = "SELECT Pre, ID, Name FROM People;"
    
    for row in cur.execute(sqlquery):
        while threading.active_count() > 20 :
            pass
        thread = Thread(target=generateCertificate, args=(row,n))
        thread.start()
        threads.append(thread)
        print(f'Active Threads: {threading.active_count()}')
        n += 1
    for thread in threads:
        thread.join()
    end = time.perf_counter()
    print(f'Finished in {round(end-start, 2)} second(s)')

def sendEmail(row, n):
    Name = row[0]
    Email = row[1]

    img_fname = f'Certificate{n}.png'
    msg = EmailMessage()
    msg['Subject'] = f'شهادة {Name}'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = Email
    msg.set_content('')

    with open(f'pictures/{img_fname}', 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def threadedEmail():
    n = 0
    threads = []
    start = time.perf_counter()
    sqlquery = "SELECT Name, Email FROM People;"
    
    for row in cur.execute(sqlquery):
        while threading.active_count() > 7 :
            pass
        thread = Thread(target=sendEmail, args=(row,n))
        thread.start()
        threads.append(thread)
        print(f'Active Threads: {threading.active_count()}')
        n += 1
    for thread in threads:
        thread.join()
    end = time.perf_counter()
    print(f'Finished in {round(end-start, 2)} second(s)')

# method:
#  thread = threading.Thread(target=threadedEmail)

def threadthreadedEmail():
    thread = Thread(target=threadedEmail)
    thread.start()

# method:
#  thread = threading.Thread(target=threadedCertificate)

def threadthreadedCertificate():
    thread = Thread(target=threadedCertificate)
    thread.start()