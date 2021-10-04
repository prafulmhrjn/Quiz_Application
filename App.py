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
    "wcwdcwcd",
    "cwdcdwcwdcwsc",
    "Tdwcdwcwdcdwc",
    "Twdwdcdwcwcdwscwscwdcw",
    "cdewverbvfrbv",
    "efvvebvebebetb",
    "efvefefverbve",
    "efveviuwdivwnv",
    "ejnvineinv"
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

answers = [1,2,3,0,3,2,1,0,3,2]

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes)<5):
        x=random.randint(0,9)
        #indexes.append(x)
        if x in indexes:
            continue
        else:
            indexes.append(x)
    #print(indexes)


def showresult(score):
    lblquestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    img2 = Image.open("C:/Users/Prafulmhrjn/Desktop/kicks/1232070.jpg")
    img2 = img2.resize((400, 400), Image.ANTIALIAS)
    photoimg2 = ImageTk.PhotoImage(img2)
    btnimg = Button(root, image=photoimg2, borderwidth=0)
    btnimg.place(x=250, y=20)

    if score >=40:
        text='you are excellent'
    elif(score >=20 and score<40):
        text='okay'
    else:
        text='bad'




def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 10
        x+=1
    print(score)
    showresult(score)




ques = 1
def selected():
    global radiovar,user_answer
    global lblquestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblquestion.config(text=questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0],
        r2['text'] = answers_choice[indexes[ques]][1],
        r3['text'] = answers_choice[indexes[ques]][2],
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1

    else:
        print(indexes)
        print(user_answer)
        calc()


#functions

def startquiz():
    global lblquestion,r1,r2,r3,r4
    lblquestion=Label(root,text=questions[indexes[0]],font=('Consolas',16))
    lblquestion.pack()

    global radiovar

    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(root,text=answers_choice[indexes[0]][0],font=('Times',12),value=0,variable=radiovar,command = selected)
    r1.pack()
    r2 = Radiobutton(root, text=answers_choice[indexes[0]][1], font=('Times', 12), value=1, variable=radiovar,command = selected)
    r2.pack()
    r3 = Radiobutton(root, text=answers_choice[indexes[0]][2], font=('Times', 12), value=2, variable=radiovar,command = selected)
    r3.pack()
    r4 = Radiobutton(root, text=answers_choice[indexes[0]][3], font=('Times', 12), value=3, variable=radiovar,command = selected)
    r4.pack()




def pressedstart():
    btnimg.destroy()
    labeltext.destroy()
    startbtn.destroy()
    gen()
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