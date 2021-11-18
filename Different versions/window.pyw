from tkinter import *
from tkinter import ttk
from csv import writer
from CertificateGenerator3 import generateCertificate, sendEmail

def btn_clicked():
    print("Button Clicked")

def whoareu():
    Email_entry.delete(0, END)

def saveInfo():
    with open('Data3.csv', 'a',encoding='UTF-8' , newline='') as f:
        all_info = []
        Pre_info = Pre.get()
        all_info += [Pre_info]
        Name_info = NName.get()
        all_info += [Name_info]
        Email_info = Email.get()
        all_info += [Email_info]
        Id_info = Id.get()
        id_info = str(Id_info)
        all_info += [Id_info]
        print(all_info)
        writero = writer(f)
        writero.writerow(all_info)
    Email_entry.delete(0, END)
    Name_entry.delete(0, END)
    ID_entry.delete(0, END)
    Pre_entry.delete(0, END)
    

window = Tk()

style = ttk.Style()

window.title("Certification Generator")

window.iconbitmap('UI/peepoSalute112.ico')

window.geometry("728x510")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 510,
    width = 728,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = "UI/background.png")
background = canvas.create_image(
    231.5, 214.5,
    image=background_img)

NName = StringVar()
Email = StringVar()
Id = IntVar()
Pre = StringVar()

Remove_btn_img = PhotoImage(file = f"UI/img0.png")
Remove_btn = Button(
    image = Remove_btn_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

Remove_btn.place(
    x = 289, y = 441,
    width = 139,
    height = 27)

Create_btn_img = PhotoImage(file = f"UI/img3.png")
Create_btn = Button(
    image = Create_btn_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = generateCertificate,
    relief = "flat")

Create_btn.place(
    x = 289, y = 475,
    width = 139,
    height = 27)

SEmail_btn_img = PhotoImage(file = f"UI/img1.png")
SEmail_btn = Button(
    image = SEmail_btn_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = sendEmail,
    relief = "flat")

SEmail_btn.place(
    x = 525, y = 441,
    width = 139,
    height = 27)

Add_btn_img = PhotoImage(file = f"UI/img2.png")
Add_btn = Button(
    image = Add_btn_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = saveInfo,
    relief = "flat")

Add_btn.place(
    x = 54, y = 441,
    width = 139,
    height = 27)

Name_entry_img = PhotoImage(file = f"UI/img_textBox0.png")
Name_entry_bg = canvas.create_image(
    223.0, 365.0,
    image = Name_entry_img)

Name_entry = Entry(
    textvariable=NName,
    bd = 0,
    bg = "#f0f0f0",
    highlightthickness = 0)

Name_entry.place(
    x = 104, y = 348,
    width = 242,
    height = 32)

Pre_entry_img = PhotoImage(file = f"UI/img_textBox0.png")
Pre_entry_bg = canvas.create_image(
    223.0, 365.0,
    image = Name_entry_img)

style.configure("TMenubutton", background=Pre_entry_bg, )

options = ["Hi" , "Hello"]

Pre_entry = OptionMenu(window ,Pre ,*options)

Pre_entry.place(
    x = 422, y = 391,
    width = 242,
    height = 32)

ID_entry_img = PhotoImage(file = f"UI/img_textBox1.png")
ID_entry_bg = canvas.create_image(
    223.0, 408.0,
    image = ID_entry_img)

ID_entry = Entry(
    textvariable=Id,
    bd = 0,
    bg = "#f0f0f0",
    highlightthickness = 0)

ID_entry.place(
    x = 104, y = 391,
    width = 242,
    height = 32)

Email_entry_img = PhotoImage(file = f"UI/img_textBox2.png")
Email_entry_bg = canvas.create_image(
    543.0, 365.0,
    image = Email_entry_img)

Email_entry = Entry(
    textvariable=Email,
    bd = 0,
    bg = "#f0f0f0",
    highlightthickness = 0)

Email_entry.place(
    x = 422, y = 348,
    width = 242,
    height = 32)


window.resizable(False, False)
window.mainloop()
