import tkinter as tk
from PIL import Image, ImageTk
import os


root = tk.Tk()
root.iconbitmap("mainicon.ico")
root.title("Cipher Encryption & Decryption ( ͡❛ ͜ʖ ͡❛)✌")
global logo
canvas = tk.Canvas(root , width = 800 , height= 400, bg="#181818")
canvas.grid(columnspan=3, rowspan=3)
bgr=ImageTk.PhotoImage(Image.open("bgimg.jpg"))
bg_label= tk.Label(root, image=bgr)
bg_label.place(x=0, y=0, relheight=1, relwidth=1)

#logo
logo = Image.open("logo.png")
logo1= ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo1)
logo_label.image= logo1
logo_label.grid(column=1 , row= 0)


#instruction
instruct =tk.Label(root , text="Select the operation you want to Perform", font="30")
instruct.grid(columnspan=3 ,column=0 , row= 3)


def open_encrypt():
    encrypt_text.set("Encrypting....")
    os.system(" python -u encrypt_main.py")
    encrypt_text.set("Encrypt Data")

def open_decrypt():
    decrypt_text.set("Decrypting...")
    os.system(" python -u decrypt_main.py")
    decrypt_text.set("Decrypt Data")


#Buttons
encrypt_text=tk.StringVar()
decrypt_text=tk.StringVar()
encrypt_btn= tk.Button(root , textvariable=encrypt_text, command=lambda:open_encrypt(), font="Raleway", bg="#000000", fg="#38E54D" ,height=2 , width=15)
decrypt_btn= tk.Button(root , textvariable=decrypt_text, command=lambda:open_decrypt(), font="Raleway", bg="#000000", fg="#38E54D" ,height=2 , width=15)
encrypt_text.set("Encrypt Data")
decrypt_text.set("Decrypt Data")
decrypt_btn.grid(column=2, row=2)
encrypt_btn.grid(column=0, row=2)

root.mainloop()