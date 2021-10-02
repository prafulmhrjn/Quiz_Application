#import the required libraries
import tkinter
from tkinter import *
from PIL import ImageTk, Image
import random



root = Tk()
root.title('Guess The Sneaker')
root['bg']='light green'
root.geometry("900x600")


questions = [
    "This is sample question 1",
    "This is sample question 2",
    "This is sample question 3",
    "This is sample question 4",
    "This is sample question 5",
    "This is sample question 6",
    "This is sample question 7",
    "This is sample question 8",
    "This is sample question 9",
    "This is sample question 10"
]

answers_choice = [
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"]

]

indexes = []
def gen():
    global indexes
    while(len(indexes)<5):
        x=random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


#functions

def startquiz():
    lblquestion=Label(root,text='This is a sample question',font=('Consolas',16))
    lblquestion.pack()

    radiovar = IntVar()
    radiovar.set(-1)

    r1 = tkinter.Radiobutton(root,text='sample choice 1',font=('Times',12),value=0,variable=radiovar)
    r1.pack()
    r2 = tkinter.Radiobutton(root, text='sample choice 2', font=('Times', 12), value=1, variable=radiovar)
    r2.pack()
    r3 = tkinter.Radiobutton(root, text='sample choice 3', font=('Times', 12), value=2, variable=radiovar)
    r3.pack()
    r4 = tkinter.Radiobutton(root, text='sample choice 4', font=('Times', 12), value=3, variable=radiovar)
    r4.pack()




def pressedstart():
    btnimg.destroy()
    labeltext.destroy()
    startbtn.destroy()
    startquiz()



#load images

img1 = Image.open("C:/Users/Prafulmhrjn/OneDrive/Desktop/dd/kicks.jpg")
img1 = img1.resize((400,400), Image.ANTIALIAS)
photoimg1 = ImageTk.PhotoImage(img1)
btnimg = Button(root, image=photoimg1, borderwidth=0)
btnimg.place(x=250, y=20)


#labels
labeltext=Label(root,text='Guess The Sneaker',font=('Algerian',24),bg='light blue')
labeltext.grid(padx=300,pady=450)

#Create the buttons
startbtn=Button(root,text='START',fg='white',font=('Algerian',20),bg='black',command=pressedstart)
startbtn.place(x=400,y=510)





root.mainloop()