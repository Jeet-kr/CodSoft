from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Rock Paper Scissor Game - JK")
root.geometry("900x800")
root.configure(background="#d9d9d9")

r = ImageTk.PhotoImage(Image.open("rock.png"))
p = ImageTk.PhotoImage(Image.open("paper.png"))
s = ImageTk.PhotoImage(Image.open("scissor.png"))
choices = [r, p, s]
 
G_won = 0
C_won = 0

def play(gamer_choice):
    global choices, G_won, C_won

    gamer.config(image=gamer_choice)
    computer_choice = random.choice(choices)
    computer.config(image=computer_choice)

    if gamer_choice == choices[0] and computer_choice == choices[0]:
        score.config(text=f'It is a tie\n Score: {G_won} of Gamer VS {C_won} of Computer', fg='orange')

    if gamer_choice == choices[0] and computer_choice == choices[1]:
        C_won += 1
        score.config(text=f'Computer Win\n Score: {G_won} of Gamer VS {C_won} of Computer', fg='red')

    if gamer_choice == choices[0] and computer_choice == choices[2]:
        G_won += 1
        score.config(text=f'Gamer Win\n Score: {G_won} of Gamer VS {C_won} of Computer', fg='green')

    if gamer_choice == choices[1] and computer_choice == choices[0]:
        G_won += 1
        score.config(text=f'Gamer Win\n Score: {G_won} of Gamer VS {C_won} of Computer', fg='green')

    if gamer_choice == choices[1] and computer_choice == choices[1]:
        score.config(text=f'It is a tie\n Score: {G_won} of Gamer VS {C_won} of Computer', fg='orange')

    if gamer_choice == choices[1] and computer_choice == choices[2]:
        C_won += 1
        score.config(text=f'Computer Win\n Score: {G_won} of Gamer VS {C_won} of Computer', fg='red')

    if gamer_choice == choices[2] and computer_choice == choices[0]:
        C_won += 1
        score.config(text=f'Computer Win\n Score: {G_won} of Gamer VS {C_won} of Computer', fg='red')

    if gamer_choice == choices[2] and computer_choice == choices[1]:
        G_won += 1
        score.config(text=f'Gamer Win\n Score: {G_won} of Gamer VS {C_won} of Computer', fg='green')

    if gamer_choice == choices[2] and computer_choice == choices[2]:
        score.config(text=f'It is a tie\n Score: {G_won} of Gamer VS {C_won} of Computer', fg='orange')
    
score = Label(root, text='Score Board: ', font=('Helvetica',14,'bold'))
score.config(bg='#d9d9d9')
score.pack(pady=10)

computer = Label(root, image=r)
computer.pack(pady=15)
computer.config(bg='#d9d9d9')
gamer = Label(root, image=r)
gamer.pack(pady=15)
gamer.config(bg='#d9d9d9')

frame = Frame(root)
frame.pack()
frame.config(bg='#d9d9d9')

btn_r = Button(frame, image=r, bd=7, command= lambda: play(choices[0]))
btn_r.config(bg='sky blue')
btn_r.grid(row=0, column=0, padx=20,pady=10)

btn_p = Button(frame, image=p, bd=7, command= lambda: play(choices[1]))
btn_p.config(bg='sky blue')
btn_p.grid(row=0, column=1, padx=20,pady=10)

btn_s = Button(frame, image=s, bd=7, command= lambda: play(choices[2]))
btn_s.config(bg='sky blue')
btn_s.grid(row=0, column=2, padx=20,pady=10)


root.mainloop()