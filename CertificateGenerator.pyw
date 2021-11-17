import os
import smtplib
import imghdr
from email.message import EmailMessage
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
import sqlite3
from threading import Thread

font = ImageFont.truetype('arial.ttf',30)

connection = sqlite3.connect("Data.sqlite")
cur = connection.cursor()

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

def reshape(something):
    reshaped_text = arabic_reshaper.reshape(something)
    bidi_text = get_display(reshaped_text)
    return bidi_text

def generateCertificate():
    n = 0
    sqlquery = "SELECT Pre, ID, Name FROM People;"
    for row in cur.execute(sqlquery):
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
        n += 1

threads = []

sqll = "SELECT * FROM People;"

for row in cur.execute(sqll):
    thread = Thread(target=generateCertificate, args=(row,))
    threads.append(thread)
    thread.start()

# for thread in threads: 
#     thread.join() # wait for completion


# with open('Data3.csv', 'r', encoding='UTF-8') as f:

#     threads = []

#     for i, studentData in enumerate(f):
#         if i == 0: continue
#         print(studentData)
#         print(i)

        #         thread = Thread(target=generateCertificate, args=(studentData,))
        #         threads.append(thread)
        #         thread.start()

        #     for thread in threads: 
        #         thread.join() # wait for completion

def sendEmail():
    sqlquery = "SELECT Name, Email FROM People;"
    
    n = 0
    for row in cur.execute(sqlquery):

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
        n += 1
threadse = []

sqlle = "SELECT * FROM People;"

for row in cur.execute(sqlle):
    threade = Thread(target=sendEmail, args=(row,))
    threadse.append(threade)
    threade.start()

# for thread in threadse: 
#     thread.join() # wait for completion
