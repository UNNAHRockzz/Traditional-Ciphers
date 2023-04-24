import tkinter
from tkinter import *
from tkinter.ttk import *
window=tkinter.Tk()
window.title("The Cipher Bonanza")
#label=tkinter.Label(window,text="The Cipher List").pack()
window.geometry('450x300')
def clicked():
    t1.configure(text="Button click")
bt=tkinter.Button(window,text="Select",command=clicked)
bt.grid(column=1,row=0)
combo=Combobox(window)
combo['values']=("Select Cipher","Ceasar Cipher","Minoalphabetic Cipher","Reverse Cipher")
combo.current(0)
combo.grid(column=0,row=0)
window.mainloop()