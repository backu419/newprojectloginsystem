import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector


def connection(filename):
    conn = mysql.connector.connect(host='localhost', user='root', password='password', port=3306, db='hcl')
    query = "select * from login where id={0}".format(filename,)
    cur = conn.cursor(prepared=True)
    cur.execute(query)

    i = 0
    for s in cur:
        for j in range(len(s)):
            e = Entry(root, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, s[j])

            e = Label(root, width=10, text=s[j],
                      borderwidth=2, relief='ridge', anchor="w")
        i = i + 1
        print(i)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def checksearch():
    f_name = un.get()
    connection(f_name)

root = tk.Tk()
root.geometry("400x400")
t = Label(root, text="Search Form", font=('arial', 14), bd=15)
t.pack()
form = Frame(root)
form.pack(side=TOP, fill=X)
un = StringVar()

sf = Label(form, text="Search:  ", font=('arial', 14), bd=15)
sf.grid(row=1, stick=W)
sf = Entry(form, textvariable=un)
sf.grid(row=1, column=2)

search = Button(root, text="search", command=checksearch)
search.pack()
root.mainloop()
