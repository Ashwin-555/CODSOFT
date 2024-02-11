from tkinter import *                          #import tkinter,Pillow and random libraries
from PIL import Image,ImageTk
from random import randint

root=Tk()
root.title("Rock-paper-scissor game")
root.configure(bg="green")
root.iconbitmap("rock-paper-scissors.ico")

#score indications
computer=Label(root,text="COMPUTER",font=50,bg="green",fg="white").grid(row=0,column=2)
player=Label(root,text="PLAYER",font=50,bg="green",fg="white").grid(row=0,column=4)
challenge=Label(root,text="VS",font=50,bg="green",fg="white").grid(row=0,column=3)


#for computer images
rock_img_cmp=ImageTk.PhotoImage(Image.open("rock_computer.png"))
paper_img_cmp=ImageTk.PhotoImage(Image.open("paper_computer.png"))
scissor_img_cmp=ImageTk.PhotoImage(Image.open("scissor_computer.png"))

#for user images
rock_user=ImageTk.PhotoImage(Image.open("rock_user.png"))
paper_user=ImageTk.PhotoImage(Image.open("paper_user.png"))
scissor_user=ImageTk.PhotoImage(Image.open("scissors_user.png"))

#create label images for rockpaper-scissor
computer_label=Label(root,image=rock_img_cmp,bg="green")
user_label=Label(root,image=rock_user,bg="green")
computer_label.grid(row=1,column=1)
user_label.grid(row=1,column=7)

#scores
computer_score=Label(root,text="0",font=100,bg="green",fg="white")
player_score=Label(root,text="0",font=100,bg="green",fg="white")
computer_score.grid(row=1,column=2)
player_score.grid(row=1,column=4)

#buttons
rock_button=Button(root,text="ROCK",width=20,height=2,bg="red",fg="white",command=lambda:choice_update("ROCK")).grid(row=3,column=2)
paper_button=Button(root,text="PAPER",width=20,height=2,bg="orange",fg="white",command=lambda:choice_update("PAPER")).grid(row=3,column=3)
scissor_button=Button(root,text="SCISSOR",width=20,height=2,bg="blue",fg="white",command=lambda:choice_update("SCISSOR")).grid(row=3,column=4)

#messages
msg=Label(root,font=50,bg="green",fg="white")
msg.grid(row=5,column=3)

choice=["ROCK","PAPER","SCISSOR"]         #choices of the game

#udate your choices
def choice_update(x):

    #for computer 
    choices=choice[randint(0,2)]
    if choices=="ROCK":
        computer_label.configure(image=rock_img_cmp)
    elif choices=="PAPER":
         computer_label.configure(image=paper_img_cmp)
    else:
        computer_label.configure(image=scissor_img_cmp)

    #for player
    if x=="ROCK":
        user_label.configure(image=rock_user)
    elif x=="PAPER":
        user_label.configure(image=paper_user)
    else:
        user_label.configure(image=scissor_user)

    check_win(x,choices)

def updatemessage(x):
    msg['text']=x

#player score updated
def update_player_score():
    score=int(player_score["text"])
    score+=1
    player_score["text"]=str(score)

#computer score updated
def update_computer_score():
    score=int(computer_score["text"])
    score+=1
    computer_score["text"]=str(score)

#to check the winner
def check_win(player,computer):
    if player==computer:
        updatemessage("It's a tie!!")

    elif player=="ROCK":
        if computer=="SCISSOR":
            updatemessage("You Win!!")
            update_player_score()
        else:
            updatemessage("Computer Wins!! better Luck next time")
            update_computer_score()

    elif player=="PAPER":
        if computer=="ROCK":
            updatemessage("You win!!")
            update_player_score()
        else:
            updatemessage("Computer Wins!! better Luck next time")
            update_computer_score()

    elif player=="SCISSOR":
        if computer=="PAPER":
            updatemessage("You win!!")
            update_player_score()
        else:
            updatemessage("Computer Wins!! better Luck next Time")
            update_computer_score()
    else:
        pass
    

root.mainloop()