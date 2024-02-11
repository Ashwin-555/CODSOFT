import tkinter as tk
from tkinter import *
from tkinter import ttk
class Todolist:
    def __init__(self):
        #creating window
        self.root=tk.Tk()
        self.root.title("MY TO-DO-LIST")
        self.root.geometry("700x600+400+100")
        self.root.iconbitmap("image1.ico")  #uploading icon

        #create labels
        self.label1=Label(self.root,text="MY TO-DO LIST APP",font=("arial",20),width=10,bd=5,bg="yellow",fg="black")
        self.label1.pack(side="top",fill=BOTH)
        self.label2=Label(self.root,text="ADD TASK",font=("arial"),width=10 ,bd=5 ,bg="sky blue",fg="black")
        self.label2.place(x=40,y=60)
        self.label3=Label(self.root,text="TASK",font=("arial"),width=10 ,bd=5 ,bg="sky blue",fg="black")
        self.label3.place(x=350,y=54)

        #create taskbox and inserting box
        self.taskbox=Listbox(self.root,height=10,bd=5,width=25,font=("Arial",20))
        self.taskbox.place(x=230,y=100)
        self.addtask=Text(self.root,height=2,width=25,bd=5,font=("Arial",10))
        self.addtask.place(x=20,y=120)

        def add_task():     #add task using the function
            content=self.addtask.get(1.0,END)
            self.taskbox.insert(END,content)
            with open("tasks.txt",'a') as file:
                file.write(content)
                file.seek(0)
                file.close()
                self.addtask.delete(1.0,END)
        
        def delete():    #delete task using the function
            delet=self.taskbox.curselection()
            look=self.taskbox.get(delet)
            with open("tasks.txt",'r+') as f:
                new_f=f.readlines()
                f.seek(0)
                for line in new_f:
                    item=str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.taskbox.delete(delet)
        with open("tasks.txt","r") as fl:
            read=fl.readlines()
            for i in read:
                k=i.split()
                self.taskbox.insert(END,k)
                fl.close()
        
        #buttons for add and delete task
        self.add_button=Button(self.root,text="ADD",font=("Arial"),width=10,bd=5,bg="red",fg="black",command=add_task)
        self.add_button.place(x=37,y=205)

        self.delete_button=Button(self.root,text="DELETE",font="Arial",width=10,bd=5,bg="red",fg="black",command=delete)
        self.delete_button.place(x=37,y=305)

        
        self.root.mainloop()

Todolist()
