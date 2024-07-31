from tkinter import *
import random
import string

root = Tk()
root.geometry("400x200")

passstr = StringVar()
pwd_len = IntVar()

def get_pass():
    pass1 = string.ascii_letters + string.digits + string.punctuation
    password = ""
    
    for x in range(pwd_len.get()): 
        password = password + random.choice(pass1)
        passstr.set(password)
        
Label(root, text="Password Generator - JK", font="calibri 18 bold").pack()
Label(root, text="Enter length of Password").pack(pady=9)
Entry(root, textvariable=pwd_len).pack(pady=2)
Button(root, text="Generate Password", command=get_pass).pack(pady=15)
Entry(root, textvariable=passstr).pack(pady=2)

root.mainloop()

