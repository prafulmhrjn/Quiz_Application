from tkinter import *
root = Tk()
root.title('Quiz Application')
root['bg']='light green'
root.geometry("1280x680")


label_m=Label(root,text='Quiz',font=('Arial',50),bg='light green')
label_m.place(x=600,y=50)
label1=Label(root,text='Username',font=('Arial',30),bg='light green')
label1.place(x=400,y=250)
entry_1=Entry(root,font=('Arial',30))
entry_1.place(x=500,y=250)
button1=Button(root,text='Submit',font=('Arial',30))
button1.place(x=600,y=350)
root.mainloop()