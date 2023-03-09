from tkinter import *
import tkinter
from PIL import ImageTk, Image
import os

root=Tk()
root.title("ZODIAC SIGN CALCULATOR")
root.geometry("520x668")
root.configure(bg="white")
result=Label(root,bg="white")
result.grid(row=4,column=0,columnspan=2)

def get_zodiac(date,month):
    global result
    result.grid_forget()
    date=int(entry1.get())
    month=int(entry2.get())
    if (month==3 and date>=21) or (month==4 and date<20):
        result=Label(root,text="YOUR ZODIAC SIGN IS ARIES",borderwidth=12,bg="white")
        result.config(font = ("Comic Sans",20))
        result.grid(row=4,column=0,columnspan=2)

        image1 = Image.open("images/aries.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=4, y=320)
    elif (month==4 and date>=20) or (month==5 and date<21):
        result=Label(root,text="YOUR ZODIAC SIGN IS TAURUS",borderwidth=12,bg="white")
        result.config(font = ("Comic Sans",20))
        result.grid(row=4,column=0,columnspan=2)

        image1 = Image.open("images/taurus.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=4, y=320)
    elif (month==5 and date>=21) or (month==6 and date<21):
        result=Label(root,text="YOUR ZODIAC SIGN IS GEMINI",borderwidth=12,bg="white")
        result.config(font = ("Comic Sans",20))
        result.grid(row=4,column=0,columnspan=2)

        image1 = Image.open("images/gemini.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=4, y=320)
    elif (month==6 and date>=21) or (month==7 and date<23):
        result=Label(root,text="YOUR ZODIAC SIGN IS CANCER",borderwidth=12,bg="white")
        result.config(font = ("Comic Sans",20))
        result.grid(row=4,column=0,columnspan=2)

        image1 = Image.open("images/cancer.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=4, y=320)
    elif (month==7 and date>=23) or (month==8 and date<23):
        result=Label(root,text="YOUR ZODIAC SIGN IS LEO",borderwidth=12,bg="white")
        result.config(font = ("Comic Sans",20))
        result.grid(row=4,column=0,columnspan=2)

        image1 = Image.open("images/leo.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=4, y=320)
    elif (month==8 and date>=23) or (month==9 and date<23):
        result=Label(root,text="YOUR ZODIAC SIGN IS VIRGO",borderwidth=12,bg="white")
        result.config(font = ("Comic Sans",20))
        result.grid(row=4,column=0,columnspan=2)

        image1 = Image.open("images/virgo.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=4, y=320)
    elif (month==9 and date>=23) or (month==10 and date<23):
        result=Label(root,text="YOUR ZODIAC SIGN IS LIBRA",borderwidth=12,bg="white")
        result.config(font = ("Comic Sans",20))
        result.grid(row=4,column=0,columnspan=2)

        image1 = Image.open("images/libra.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=4, y=320)
    elif (month==10 and date>=23) or (month==11 and date<22):
        result=Label(root,text="YOUR ZODIAC SIGN IS SCORPIO",borderwidth=12,bg="white")
        result.config(font = ("Comic Sans",20))
        result.grid(row=4,column=0,columnspan=2)

        image1 = Image.open("images/scorpio.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=4, y=320)
    elif (month==11 and date>=22) or (month==12 and date<22):
        result=Label(root,text="YOUR ZODIAC SIGN IS SAGITTARIUS",borderwidth=12,bg="white")
        result.config(font = ("Comic Sans",20))
        result.grid(row=4,column=0,columnspan=2)

        image1 = Image.open("images/sagittarius.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=4, y=320)
    elif (month==12 and date>=22) or (month==1 and date<20):
        result=Label(root,text="YOUR ZODIAC SIGN IS CAPRICORN",borderwidth=12,bg="white")
        result.config(font = ("Comic Sans",20))
        result.grid(row=4,column=0,columnspan=2)

        image1 = Image.open("images/capricorn.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=4, y=320)
    elif (month==1 and date>=20) or (month==2 and date<19):
        result=Label(root,text="YOUR ZODIAC SIGN IS AQUARIUS",borderwidth=12,bg="white")
        result.config(font = ("Comic Sans",20))
        result.grid(row=4,column=0,columnspan=2)

        image1 = Image.open("images/aquarius.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=4, y=320)
    elif (month==2 and date>=19) or (month==3 and date<21):
        result=Label(root,text="YOUR ZODIAC SIGN IS PISCES",borderwidth=12,bg="white")
        result.config(font = ("Comic Sans",20))
        result.grid(row=4,column=0,columnspan=2)

        image1 = Image.open("images/pisces.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=4, y=320)
    else:
        result=Label(root,text="Invalid Input",borderwidth=12,bg="white")
        result.config(font = ("Comic Sans",20))
        result.grid(row=4,column=0,columnspan=2)

        image1 = Image.open("images/greenu.png")
        image2 = image1.resize((508,339), Image.LANCZOS)
        test = ImageTk.PhotoImage(image2)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=4, y=320)

label1=Label(root,text="WELCOME TO ZODIAC SIGN CALCULATOR ",borderwidth=18,bg="black",fg="white")
label1.config(font=("Comic Sans",17))
label1.grid(row=0,column=0,columnspan=2)
label3=Label(root,text="BIRTH MONTH :",borderwidth=25,bg="white")
label3.config(font=("Comic Sans",17))
label3.grid(row=1,column=0)
label2=Label(root,text="BIRTH DATE :",borderwidth=25,bg="white")
label2.config(font=("Comic Sans",17))
label2.grid(row=2,column=0)
entry1=Entry(root,borderwidth=3,width=7)
entry2=Entry(root,borderwidth=3,width=7)
entry1.grid(row=2,column=1)
entry2.grid(row=1,column=1)
date=entry1.get()
month=entry2.get()
get_button=Button(root,text="GET ZODIAC SIGN",anchor=CENTER,command=lambda:get_zodiac(date,month),height=2,width=20,bg="black",fg="white")

get_button.grid(row=3,column=0,columnspan=2)
root.mainloop()