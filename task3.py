from tkinter import *   #import tkinter module
import string           #importing both string and random module
import random

root=Tk()
root.title("Password Generator 2024")            #add title to the window
root.geometry("500x600")
root.iconbitmap("image2.ico")                    #creating an icon for the window
root.config(bg="red")
choice=IntVar()
Fonts=("arial",17,"bold")

label=Label(root,text="Best Password Generator",font=("helvetica",20,"bold"),bg="red",fg="white")
label.grid(padx=75,pady=15)

def generator():                                                     #func for generation of password
    lowercase=string.ascii_uppercase
    uppercase=string.ascii_lowercase
    numbers=string.digits
    punctuation=string.punctuation
    all=lowercase+uppercase+numbers+punctuation
    password_length=int(enter_length.get())
    
    if choice.get()==1:
        password=random.sample(lowercase,password_length)              #using random library and sample method
        passwordgenerate.insert(0,password)
    if choice.get()==2:
        password=random.sample(lowercase+uppercase,password_length)
        passwordgenerate.insert(0,password)
    if choice.get()==3:
        password=random.sample(all,password_length)
        passwordgenerate.insert(0,password)

#create radio buttons
weakbutton=Radiobutton(root,text="Weak",font=Fonts,variable=choice,value=1)
weakbutton.grid(pady=7)
mediumbutton=Radiobutton(root,text="Medium",font=Fonts,variable=choice,value=2)
mediumbutton.grid(pady=7)
strongbutton=Radiobutton(root,text="Strong",font=Fonts,variable=choice,value=3)
strongbutton.grid(pady=7)

length=Label(root,text="Password length",font=Fonts,bg="red",fg="white")
length.grid(padx=75,pady=15)

enter_length=Entry(root,font=("arial",13),width=10)  # enter length box
enter_length.grid(pady=5)

generate=Button(root,text="Generate",font=Fonts,command=generator)      #generate password
generate.grid(pady=5)

passwordgenerate=Entry(root,font=("arial",15),width=40)            #display of password
passwordgenerate.grid(pady=5)

root.mainloop()