from tkinter import *
from tkinter import ttk
from views import *
from tkinter import messagebox

color1="blue"
color2="white"
color3="black"

root=Tk()
root.title("Contact Book App")
root.geometry("485x450")
root.config(bg=color2)
root.resizable(width=FALSE,height=FALSE)


#frames
frame_up=Frame(root,width=500,height=50,bg=color1)
frame_up.grid(row=0,column=0,padx=0,pady=1)

frame_down=Frame(root,width=500,height=150,bg=color2)
frame_down.grid(row=1,column=0,padx=0,pady=1)

frame_tab=Frame(root,width=500,height=100,bg=color2,relief="flat")
frame_tab.grid(row=2,column=0,columnspan=2,padx=0,pady=1,sticky=NW)

#functions
def show():
    global tree 
    list_header=["Name","Phone","Email","Address"]
    tree=ttk.Treeview(frame_tab,selectmode="extended",columns=list_header,show="headings")
    vsb=ttk.Scrollbar(frame_tab,orient="vertical",command=tree.yview)
    hsb=ttk.Scrollbar(frame_tab,orient="horizontal",command=tree.xview)
    tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)

    demo_list=view()

    tree.grid(row=0,column=0,sticky="nsew")
    vsb.grid(row=0,column=1,sticky="ns")
    hsb.grid(row=1,column=0,sticky="ew")
    
    tree.heading(0,text="Name",anchor=NW)
    tree.heading(1,text="Phone",anchor=NW)
    tree.heading(2,text="Email",anchor=NW)
    tree.heading(3,text="Address",anchor=NW)

    tree.column(0,width=120,anchor=NW)
    tree.column(1,width=50,anchor=NW)
    tree.column(2,width=100,anchor=NW)
    tree.column(3,width=180,anchor=NW)

    for items in demo_list:
        tree.insert("","end",values=items)

show()

def insert():
    name = e_name.get()
    phone = e_phone.get()
    email=e_email.get()
    address = e_address.get()
    data = [name,phone,email,address]
    if name =="" or phone =="" or email =="" or address =="":
           messagebox.showwarning("data","Please fill in the fields")
    else:
        add(data)
        messagebox.showinfo("data","data added successfully")

        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        e_address.delete(0, 'end')
        e_email.delete(0, 'end')
        show()
def to_update():
    try:
      tree_data = tree.focus()
      tree_dictionary = tree.item(tree_data)
      tree_list = tree_dictionary['values']
      name = str(tree_list[0])
      phone = str(tree_list[1])
      email = str(tree_list[2])
      address = str(tree_list [3]) 

      e_name.insert(0, name)
      e_phone.insert(0, phone)
      e_email .insert(0, email)
      e_address.insert(0, address)
      def confirm():
        new_name = e_name.get()
        new_phone = e_phone.get()
        new_email=e_email.get()
        new_address = e_address.get()
        data = [new_phone,new_name, new_phone, new_email, new_address]
        update(data)
        messagebox.showinfo("Success","data updated successfully")
        e_name.delete(0,'end')
        e_phone.delete(0,'end')
        e_email.delete(0,'end')
        e_address.delete(0,'end')
        for widget in frame_tab.winfo_children():
            widget.destroy()
        b_confirm.destroy()
        show()
      b_confirm = Button(frame_down, text="Confirm", width=10, height=1, bg=color1, fg = color3,font=('Ivy 8 bold'),command=confirm)
      b_confirm.place(x = 290, y = 110)
    except IndexError:
        messagebox.showerror('Error', 'Select one of them from the table')

def to_remove():
    try:
      tree_data = tree.focus()
      tree_dictionary = tree.item(tree_data)
      tree_list = tree_dictionary['values']
      tree_telephone = str(tree_list[2])
      remove(tree_telephone)
      messagebox.showinfo('Success', 'Data has been deleted successfully')
      for widget in frame_tab.winfo_children():
          widget.destroy()
      show()
    except IndexError:
        messagebox.showinfo("Error","Select one of them from the table")
    show()
def to_search():
    telephone = e_search.get()
    data = search (telephone)
    def delete_command():
      tree.delete(*tree.get_children())
    delete_command()
    for item in data:
        tree.insert('', 'end', values = item)
#frame up widgets
name=Label(frame_up,text="WORLD CONTACT BOOK",height=1,font=("verdana 17 bold"),fg=color2,bg=color1)
name.place(x=20,y=10)

#frame down widgets
l_name=Label(frame_down,text="NAME *",width=20,height=1,font=("Ivy 10"),bg=color2,anchor=NW,fg=color3)
l_name.place(x=10,y=20)

e_name=Entry(frame_down,width=25,justify="left",highlightthickness=1,relief="solid")
e_name.place(x=80,y=20)

l_phone=Label(frame_down,text="PHONE *",width=20,height=1,font=("Ivy 10"),bg=color2,anchor=NW,fg=color3)
l_phone.place(x=10,y=50)
e_phone=Entry(frame_down,width=27,justify="left",highlightthickness=1,relief="solid")
e_phone.place(x=80,y=50)

l_email=Label(frame_down,text="EMAIL *",height=1,font=("Ivy 10"),bg=color2,anchor=NW,fg=color3)
l_email.place(x=10,y=80)
e_email=Entry(frame_down,width=27,justify="left",highlightthickness=1,relief="solid")
e_email.place(x=80,y=80)

l_address=Label(frame_down,text="ADDRESS *",height=1,font=("Ivy 10"),bg=color2,anchor=NW,fg=color3)
l_address.place(x=10,y=110)
e_address=Entry(frame_down,width=27,justify="left",highlightthickness=1,relief="solid")
e_address.place(x=80,y=110)

#buttons
b_search=Button(frame_down,text="Search",height=1,bg=color1,fg="white",font=("Ivy 8 bold"),command=to_search)
b_search.place(x=290,y=20)
e_search=Entry(frame_down,width=16,justify="left",highlightthickness=1,relief="solid",font=("Ivy 11"))
e_search.place(x=347,y=20)

b_view=Button(frame_down,text="View",height=1,bg=color1,fg="white",width=10,font=("Ivy 8 bold"),command=show)
b_view.place(x=290,y=50)
b_add=Button(frame_down,text="Add",height=1,bg=color1,fg="white",width=10,font=("Ivy 8 bold"),command=insert)
b_add.place(x=400,y=50)
b_update=Button(frame_down,text="Update",height=1,bg=color1,fg="white",width=10,font=("Ivy 8 bold"),command=to_update)
b_update.place(x=400,y=80)
b_delete=Button(frame_down,text="Delete",height=1,bg=color1,fg="white",width=10,font=("Ivy 8 bold"),command=to_remove)
b_delete.place(x=400,y=110)






root.mainloop()