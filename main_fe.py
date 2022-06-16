#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import main_stl
import main_gcode
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title('TotalSTL')
window.geometry('300x200+75+75')
#window.iconbitmap('icon.ico')

window.geometry("900x800")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    900.0,
    41.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    384.0,
    9.0,
    anchor="nw",
    text="Total_STL",
    fill="#000000",
    font=("Inter", 24 * -1)
)

def button_1():
    okno =Tk()
    def exit():
        okno.destroy()
    okno.title('Information')
    ttk.Label(okno, text="TotalSTL").pack()
    ttk.Label(okno, text="version: 0.0.2").pack()
    ttk.Label(okno, text="Author: Piotr Pawlik").pack()
    ttk.Label(okno, text="Jest to oprogramowanie pozwalajace na wyswietlanie plikow .STL, zarządzanie nimi i przeglądanie plikow .GCODE dla drukarek 3D").pack()
    ttk.Button(okno, text="EXIT", command=exit).pack()

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=button_1,
    relief="flat"
)
button_1.place(
    x=744.0,
    y=7.0,
    width=80.0,
    height=25.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=main_stl.STL_view,
    relief="flat"
)
button_2.place(
    x=7.0,
    y=8.0,
    width=62.039268493652344,
    height=25.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=main_gcode.GCODE,
    relief="flat"
)
button_3.place(
    x=79.0,
    y=8.0,
    width=81.0,
    height=25.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=sys.exit,
    relief="flat"
)
button_4.place(
    x=827.0,
    y=7.0,
    width=53.0,
    height=25.0
)

canvas.create_rectangle(
    432.0,
    41.0,
    467.0,
    800.0,
    fill="#000000",
    outline="")
window.resizable(False, False)
window.mainloop()