from tkinter import *

root = Tk()
root.iconbitmap("encicon.ico")
canvas =Canvas(root , width = 800 , height= 400, bg="#181818")
canvas.grid(columnspan=7, rowspan=3)

#Labels
lab1=Label(text="Enter the text 👉", font="20", bg="#181818", fg="white")
lab1.grid(column=0, row=0)
lab2=Label(text="Encrypted Text 👉", font="20", bg="#181818", fg="white")
lab2.grid(column=0, row=2)
output_text= Label(text='',width=45,height=5)
output_text.grid(column=2, row=2)

input_text= Text( root , width=45,height=5)
input_text.grid(column=2, row=0)


clear_btn=Button(root , text="CLEAR" ,command=lambda:clear(),  bg="#000000", fg="#38E54D" ,height=2 , width=15)
clear_btn.grid(column=6, row=1)

caesar_encrypt = Button(root , text="Caesar Encrypt" , command=lambda:ciesar(input_text.get(1.0, END)), bg="#000000", fg="#38E54D" ,height=2 , width=15)
caesar_encrypt.grid(column=0, row=1)

mono_encrypt= Button(root , text="Monoalphabetic Encrypt" , command=lambda:monoalphabetic(input_text.get(1.0, END)),bg="#000000", fg="#38E54D" ,height=2 , width=20)
mono_encrypt.grid(column=2, row=1)

rev_encrypt = Button(root , text="Reverse Encrypt" , command=lambda:reverse(input_text.get(1.0, END)),bg="#000000", fg="#38E54D" ,height=2 , width=15)
rev_encrypt.grid(column=4, row=1)


def clear():
    input_text.delete(1.0, END)

#reverse cyphers
def reverse(string):
    l=[]
    l2=[]
    str=""
    l[:0]=string
    for i in l[::-1]:
        if(i==" "):
            l2.append(chr(32))
        else:
            l2.append(i)
    output_text.config(text=(str.join(l2)))
    print(str.join(l2))

#MONOALPHA CYPHER 
def monoalphabetic(string):
    l=[]
    l2=[]
    str=""
    l[:0]=string
    for i in l:
        if(i==" "):
            l2.append(chr(32))
        else:
            if(i<='m' or i<='M'):
                l2.append(chr(ord(i)+13))
            else:
                l2.append(chr(ord(i)-13))
    output_text.config(text=str.join(l2))
    print(str.join(l2))


#CAESAR CYPHER
def ciesar(string):
    l=[]
    l2=[]
    str=""
    l[:0]=string
    for i in l:
        if(i==" "):
            l2.append(chr(32))
        else:
            l2.append(chr(ord(i)+3))
    output_text.config(text=str.join(l2))
    print(str.join(l2))




root.mainloop()
