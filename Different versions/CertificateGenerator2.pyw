from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display

font = ImageFont.truetype('arial.ttf',14)


def reshape(something):
    reshaped_text = arabic_reshaper.reshape(something)
    bidi_text = get_display(reshaped_text)
    return bidi_text

with open('Data2.csv', 'r', encoding='UTF-8') as f:
    for i, line in enumerate(f):
        if i == 0: continue
        School, Student, Year, Teacher, Supervisor, Manager = line.strip().split(',')
        img = Image.open('samples/Certificate Image 2.jpg')
        bidi_School = reshape(School)
        bidi_Student = reshape(Student)
        bidi_Year = reshape(Year)
        bidi_Teacher = reshape(Teacher)
        bidi_Supervisor = reshape(Supervisor)
        bidi_Manager = reshape(Manager)
        draw = ImageDraw.Draw(img)

        xSchool, ySchool = (410, 170)
        xStudent, yStudent = (230, 170)
        xYear, yYear = (430, 210)
        xTeacher, yTeacher = (480, 315)
        xSupervisor, ySupervisor = (290, 315)
        xManager, yManager = (100, 315)

        wSchool, hSchool = draw.textsize(bidi_School, font=font)
        wStudent, hStudent = draw.textsize(bidi_Student, font=font)
        wYear, hYear = draw.textsize(bidi_Year, font=font)
        wTeacher, hTeacher = draw.textsize(bidi_Teacher, font=font)
        wSupervisor, hSupervisor = draw.textsize(bidi_Supervisor, font=font)
        wManager, hManager = draw.textsize(bidi_Manager, font=font)

        draw.text(xy=(xSchool-wSchool, ySchool), text=f'{bidi_School}', fill=(0,0,0), font=font)
        draw.text(xy=(xStudent-wStudent, yStudent), text=f'{bidi_Student}', fill=(0,0,0), font=font)
        draw.text(xy=(xYear-wYear, yYear), text=f'{bidi_Year}', fill=(0,0,0), font=font)
        draw.text(xy=(xTeacher-wTeacher, yTeacher), text=f'{bidi_Teacher}', fill=(0,0,0), font=font)
        draw.text(xy=(xSupervisor-wSupervisor, ySupervisor), text=f'{bidi_Supervisor}', fill=(0,0,0), font=font)
        draw.text(xy=(xManager-wManager, yManager), text=f'{bidi_Manager}', fill=(0,0,0), font=font)

        img_fname = f'{Student} \'s Certificate {str(i)} a.png'
        img.save(f'pictures/{img_fname}')