import threading
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image, ImageFilter, ImageEnhance
import requests
import random

root=Tk()
root.title('Валентино4ка')
root.iconbitmap('E:\Downloads\pngwing.ico.ico')
root.geometry('800x700')
root.resizable(0,0)

def getting_compliments():
    url="https://raw.githubusercontent.com/kalizzies/valentino4ka/main/phrases"
    try:
        response = requests.get(url)
        response.raise_for_status()
        quotes=response.text.splitlines()
        return quotes
    except requests.exceptions.RequestException as e:
        messagebox.showinfo("помянем",'включи интернет')
        return[]


heartimg0=Image.open('E:\Downloads\pngwing.com.png')
heartimg=ImageTk.PhotoImage(file='E:\Downloads\pngwing.com.png')

current_img = heartimg

def animate_heart():
    blur_level=0
    color_level = 1.0
    blur_level += 1
    color_level -= 1.0
    imgcopy = heartimg0.copy()

    if blur_level <= 80:
        blurimg = imgcopy.filter(ImageFilter.GaussianBlur(blur_level))
        enhancer = ImageEnhance.Color(blurimg)
        colorimage = enhancer.enhance(color_level)
        finalimg = ImageTk.PhotoImage(colorimage)
        heartbutton.config(image=finalimg)
        heartbutton.image = finalimg
        root.after(2, animate_heart)

def load_and_show_quotes():
    quotes = getting_compliments()
    if quotes:
        quote=random.choice(quotes)
    messagebox.showinfo("держи, любимка <3", quote)

def popup():
    threading.Thread(target=load_and_show_quotes).start()
heartbutton=(Button(root, height=550, width=580, image=heartimg, bd=0, text="жмякни на сердечко", font='TimesNewRoman 16', compound=BOTTOM,command=lambda:[animate_heart(),popup()]))
heartbutton.place(x=110, y=50)

root.mainloop()
