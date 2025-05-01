import threading
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image, ImageFilter, ImageEnhance
import requests
import random

import sys, os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root=Tk()
root.title('Валентино4ка')
root.iconbitmap(resource_path("pngwing.ico.ico"))
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

heartimg0 = Image.open(resource_path("pngwing.com.png"))
heartimg = ImageTk.PhotoImage(heartimg0)

current_img = heartimg

def animate_heart(blur_level=0, color_level = 1.0):

    imgcopy = heartimg0.copy()

    if blur_level <= 4 and color_level >= 0:
        blurimg = imgcopy.filter(ImageFilter.GaussianBlur(blur_level))
        enhancer = ImageEnhance.Color(blurimg)
        colorimage = enhancer.enhance(color_level)
        finalimg = ImageTk.PhotoImage(colorimage)
        heartbutton.config(image=finalimg)
        heartbutton.image = finalimg
        root.after(20, lambda: animate_heart(blur_level + 0.5, color_level-0.2))

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
