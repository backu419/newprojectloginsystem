import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector


def connection(user, passw):
    conn = mysql.connector.connect(host='localhost', user='root', password='password', port=3306, db='hcl')
    query = "select username from login where username like'%{0}'".format(user, )
    cur = conn.cursor(prepared=True)
    cur.execute(query)
    result = cur.fetchone()
    if result:
        messagebox.showinfo(title="Hello user", message="""Already user registed with same username try with another""")
    else:
        # q = """insert into login(username, password) values ('{0}','{1}')""".format(user, passw)
        q1="insert into login(username,password) values(?,?)"
        val=(user,passw)

        cur.execute(q1,val)
        conn.commit()


    cur.close()
    conn.close()
    return result


def checkfornewentry():
    u_name = un.get()
    pass_word1 = pw1.get()
    pass_word2 = pw2.get()
    print(u_name)
    print(pass_word2)
    if (pass_word1 == pass_word2):
        pass_word = pass_word1
    else:
        messagebox.showinfo(title="Hello user", message="incorrect entry")
    connection(u_name, pass_word)


root = tk.Tk()
root.geometry("400x400")
t = Label(root, text="Login registration Form", font=('arial', 14), bd=15)
t.pack()
form = Frame(root)
form.pack(side=TOP, fill=X)
un = StringVar()
pw1 = StringVar()
pw2 = StringVar()

nameL = Label(form, text="Username: ", font=('arial', 14), bd=15)
passL1 = Label(form, text="Type Password  : ", font=('arial', 14), bd=15)
passL2 = Label(form, text="Retype Password: ", font=('arial', 14), bd=15)
nameL.grid(row=1, stick=W)
passL1.grid(row=2, stick=W)
passL2.grid(row=3, stick=W)
nameE = Entry(form, textvariable=un)
passE1 = Entry(form, textvariable=pw1)
passE2 = Entry(form, textvariable=pw2, show="*")

nameE.grid(row=1, column=2)
passE1.grid(row=2, column=2)
passE2.grid(row=3, column=2)
login = Button(root, text="Register", command=checkfornewentry)
login.pack()
root.mainloop()
