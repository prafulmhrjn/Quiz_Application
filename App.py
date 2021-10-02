#import the required libraries
from tkinter import *
from PIL import ImageTk, Image



root = Tk()
root.title('Guess The Sneaker')
root['bg']='light green'
root.geometry("900x600")

#load images

img1 = Image.open("C:/Users/Prafulmhrjn/OneDrive/Desktop/dd/kicks.jpg")
img1 = img1.resize((400,400), Image.ANTIALIAS)
photoimg1 = ImageTk.PhotoImage(img1)
btn = Button(root, image=photoimg1, borderwidth=0)
btn.place(x=250, y=20)


#labels
labeltext=Label(root,text='Guess The Sneaker',font=('Algerian',24),bg='light blue')
labeltext.grid(padx=300,pady=450)

#Create the buttons
startbtn=Button(root,text='START',fg='white',font=('Algerian',20),bg='black')
startbtn.place(x=400,y=510)





root.mainloop()