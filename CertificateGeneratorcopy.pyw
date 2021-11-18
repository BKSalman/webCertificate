import os
import smtplib
import imghdr
from email.message import EmailMessage
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
import sqlite3
from threading import Thread, Lock

font = ImageFont.truetype('arial.ttf',30)

connection = sqlite3.connect("Data.sqlite", check_same_thread=False)
cur = connection.cursor()

sqlquery = "SELECT * FROM People;"

mainPre = ''
mainID = ''
mainName = ''
mainEmail = ''

for row in cur.execute(sqlquery):
    mainPre += (row[0]) + ','
    mainID += (row[1]) + ','
    mainName += (row[2]) + ','
    mainEmail += (row[3]) + ','
    # print(row[0])
mainPre = (mainPre,)
print(f'{mainPre}')

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

def reshape(something):
    reshaped_text = arabic_reshaper.reshape(something)
    bidi_text = get_display(reshaped_text)
    return bidi_text

# def generateCertificate(mainPre,mainID,mainName):
#     threads = []

#     sqll = "SELECT * FROM People;"
#     lock = Lock()
#     lock.acquire(True)
#     exee = cur.execute(sqll)
#     for Pre, Id, Name in (mainPre), (mainID), (mainName):
#         thread = Thread(target=generateCertificate, args=(Pre,Id,Name))
#         threads.append(thread)
#         thread.start()
#     lock.release()
    
#     n = 0
    
#     for Pre, Id, Name in (mainPre), (mainID), (mainName):
#         img = Image.open('samples/Certificate Image 3.jpg')
#         bidi_Pre = reshape(Pre)
#         bidi_Name = reshape(Name)
#         draw = ImageDraw.Draw(img)

#         xPosition, yPosition = (730, 300)
#         xName, yName = (700, 300)
#         xId, yId = (205, 300)

#         wPosition, _ = draw.textsize(bidi_Pre, font=font)
#         wName, _ = draw.textsize(bidi_Name, font=font)
#         wId, _ = draw.textsize(Id, font=font)

#         draw.text(xy=(xPosition-wPosition, yPosition), text=f'{bidi_Pre}', fill=(0,0,0), font=font)
#         draw.text(xy=(xName-wName, yName), text=f'{bidi_Name}', fill=(0,0,0), font=font)
#         draw.text(xy=(xId-wId, yId), text=f'{Id}', fill=(0,0,0), font=font)

#         img_fname = f'Certificate{n}.png'
#         img.save(f'pictures/{img_fname}')
#         n += 1

for Pre in mainPre:
    print(Pre)

def sendEmail():
    n = 0
    sqlquery = "SELECT Name, Email FROM People;"
    
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

# with open('Different versions/Data3.csv', 'r', encoding='UTF-8') as f:

#     threads = []

#     for i, studentData in enumerate(f):
#         if i == 0: continue
#         # print((studentData,))
#         thread = Thread(target=generateCertificate, args=(studentData,))
#         threads.append(thread)
#         thread.start()
        
    # for thread in threads: 
    #     thread.join() # wait for completion




# for thread in threads:
#     thread.join() # wait for completion

# threadse = []

# sqlle = "SELECT * FROM People;"

# for row in cur.execute(sqlle):
#     roww = ','.join(row)
#     threade = Thread(target=sendEmail, args=(roww,))
#     threadse.append(threade)
#     threade.start()

# for thread in threadse: 
#     thread.join() # wait for completion
