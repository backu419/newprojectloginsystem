import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector


def connection(user, passw):
    conn = mysql.connector.connect(host='localhost', user='root', password='password', port=3306, db='hcl')
    query = "select id from login where username =%s and password =%s"
    vals = (user, passw)
    cur = conn.cursor(prepared=True)
    cur.execute(query, vals)
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result


def check():
    u_name = un.get()
    pass_word = pw.get()
    data = connection(u_name, pass_word)
    # print(data)
    # print(data[0])
    if data is not None:
        messagebox.showinfo(title="Hello user", message="welcome")
    else:
        messagebox.showinfo(title="Hello user", message="please enter correct credentials")


root = tk.Tk()
root.geometry("400x400")
t = Label(root, text="Login Form", font=('arial', 14), bd=15)
t.pack()
form = Frame(root)
form.pack(side=TOP, fill=X)
un = StringVar()
pw = StringVar()

nameL = Label(form, text="Username: ", font=('arial', 14), bd=15)
passL = Label(form, text="Password: ", font=('arial', 14), bd=15)
nameL.grid(row=1, stick=W)
passL.grid(row=2, stick=W)
nameE = Entry(form, textvariable=un)
passE = Entry(form, textvariable=pw, show="*")
nameE.grid(row=1, column=2)
passE.grid(row=2, column=2)
login = Button(root, text="Login", command=check)
login.pack()
root.mainloop()
