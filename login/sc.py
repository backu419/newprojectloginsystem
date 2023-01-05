import mysql.connector
import tkinter as tk
from tkinter import *
conn = mysql.connector.connect(host='localhost', user='root', password='password', port=3306, db='hcl')
cur = conn.cursor()
root = tk.Tk()
root.geometry("400x200")
l1 = tk.Label(root,  text='Enter ID to search: ', width=25 )
l1.grid(row=1, column=1)
t1 = tk.Text(root,  height=1, width=4,bg='yellow')
t1.grid(row=1,column=2)
b1 = tk.Button(root, text='Show Details', width=15,bg='red', command=lambda: my_details(t1.get('1.0',END)))
b1.grid(row=1,column=4)
search = tk.StringVar()
l2 = tk.Label(root,  textvariable=search, width=30,fg='red' )
l2.grid(row=3,column=1,columnspan=2)
search.set("")
def my_details(id):
    try:
        val = int(id) # check input is integer or not
        try:
            cur.execute("SELECT * FROM login WHERE id="+id)
            result = cur.fetchone()
            search.set(result)
        except :
             search.set("Database error")
    except:
        search.set("Check input")
root.mainloop()