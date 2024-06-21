import string 
from random import randint, choice
from tkinter import *


def generate_password():
    password_min=6
    password_max=12
    all_chars =string.ascii_letters + string.punctuation  + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min,password_min)) )
    password_entry.delete(0,END)
    password_entry.insert(0,password)


window = Tk()
window.title("GENERATOR OF CODE")
window.geometry=("720x480")
window.config(background='#5061A1')

frame=Frame(window, bg='#5061A1')

width = 500
height = 500
#image =PhotoImage(file="lock.png").zoom(8).subsample(10)
canvas =Canvas(window,width=width,height=height,bg='#5061A1',bd=0, highlightthickness=0)
#canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

right_frame = Frame(frame, bg='#9076A1')

label_title = Label(right_frame,text="Mot de passe", font=("Helvetica",20), bg='#5061A1',fg='white')
label_title.pack()

label_titl = Label(text="CODE",fg='red')


password_entry  = Entry(right_frame, font=("Helvetica",20), bg='#5061A1',fg='white')
password_entry.pack()

generatecode = Button(right_frame,text="Generer",font=("Helvetica",20), bg='#0067A1',fg='white',command=generate_password)
generatecode.pack(fill=X)

right_frame.grid(row=0,column=1,sticky=W)

frame.grid()


window.mainloop()