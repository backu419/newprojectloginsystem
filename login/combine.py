from tkinter import *
from login import
from register import
from searching import

window = Tk()
window.geometry("400x400")
window.title("HCL EMP system")
menubar=Menu(window)
menubar.add_command(label="Login",command=main1)
menubar.add_command(label="New user",command=main2)
menubar.add_command(label="Search",command=main3)
window.config(menu=menubar)
window.mainloop()