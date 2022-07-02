from tkinter import *
import random

root = Tk()
root.title("RPS")
width = 600
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#9b59b6")

player_rock = PhotoImage(file='img/rock-user.png')
player_paper = PhotoImage(file='img/paper-user.png')
player_scissors = PhotoImage(file='img/scissors-user.png')
comp_rock = PhotoImage(file='img/rock-comp.png')
comp_paper = PhotoImage(file='img/paper-comp.png')
comp_scissors = PhotoImage(file='img/scissors-comp.png')
start = PhotoImage(file='img/start.png').subsample(5)
win = PhotoImage(file='img/win.png').subsample(5)
draw = PhotoImage(file='img/draw.png').subsample(5)
lose = PhotoImage(file='img/lose.png').subsample(5)

player_img = Label(root, image=player_rock, bg='#9b59b6')
player_img.grid(row=2, column=1, padx=30, pady=20)
comp_img = Label(root, image=comp_rock, bg='#9b59b6')
comp_img.grid(row=2, column=3, padx=30, pady=20)

# Lbl Player
lbl_player = Label(root, font=("Arial", 15), text='Player', bg='#9b59b6', fg='white')
lbl_player.grid(row=1, column=1)

# Lbl Comp
lbl_comp = Label(root, font=("Arial", 15), text='Comp', bg='#9b59b6', fg='white')
lbl_comp.grid(row=1, column=3)

# Score
player_score = Label(root, text='0', font=('Arial', 30), bg='#9b59b6', fg='white')
breaklbl = Label(root, text='-', font=('Arial', 30), bg='#9b59b6', fg='white')
comp_score = Label(root, text='0', font=('Arial', 30), bg='#9b59b6', fg='white')
player_score.grid(row=3, column=1)
breaklbl.grid(row=3, column=2)
comp_score.grid(row=3, column=3)

# Message
msg = Label(root, font=('Arial', 30), bg='#9b59b6', fg='#CC9900')
msg.grid(row=2, column=2)
msg.configure(image=start)

# Update Player Score
def updatePlayerScore():
    score = int(player_score['text'])
    score += 1
    player_score['text'] = score

# Update Computer Score
def updateCompScore():
    score = int(comp_score['text'])
    score += 1
    comp_score['text'] = score

# Logic
def Rock():
    global player_choice
    player_choice = 1 
    player_img.configure(image=player_rock)
    MatchProcess()

def Paper():
    global player_choice
    player_choice = 2
    player_img.configure(image=player_paper)
    MatchProcess()

def Scissors():
    global player_choice
    player_choice = 3
    player_img.configure(image=player_scissors)
    MatchProcess()

def MatchProcess():
    comp_choice = random.randint(1, 3) 
    if comp_choice == 1:
        comp_img.configure(image=comp_rock)
        ComputerRock()
    elif comp_choice == 2:
        comp_img.configure(image=comp_paper)
        ComputerPaper()
    else:
        comp_img.configure(image=comp_scissors)
        ComputerScissors()

def ComputerRock():
    if player_choice == 1:
        msg.configure(image=draw)
        
    elif player_choice == 2:
        msg.configure(image=win)
        updatePlayerScore()
    else:
        msg.configure(image=lose)
        updatePlayerScore()

def ComputerPaper():
    if player_choice == 1:
        msg.configure(image=lose)
        updateCompScore()
    elif player_choice == 2:
        msg.configure(image=draw)
    else:
        msg.configure(image=win)
        updatePlayerScore()

def ComputerScissors():
    if player_choice == 1:
        msg.configure(image=win)
        updatePlayerScore()
    elif player_choice == 2:
        msg.configure(image=lose)
        updateCompScore()
    else:
        msg.configure(image=draw)

def ExitApp():
    root.destroy()
    exit()

sm_player_rock = player_rock.subsample(3, 3)
rock = Button(root, image=sm_player_rock, command=Rock, bg='red')
rock.grid(row=4, column=1)

sm_player_paper = player_paper.subsample(3, 3)
paper = Button(root, image=sm_player_paper, command=Paper, bg='red')
paper.grid(row=4, column=2)


sm_player_scissors = player_scissors.subsample(3, 3)
scissors = Button(root, image=sm_player_scissors, command=Scissors, bg='red')
scissors.grid(row=4, column=3)

root.mainloop()