#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import sys


window = tk.Tk()
window.title('TotalSTL')
window.geometry('1000x800+50+50')
window.iconbitmap('icon.ico')



def button_clicked():
    okno =tk.Tk()
    def exit():
        okno.destroy()
    okno.title('Information')
    okno.geometry('800x100+5+5')
    ttk.Label(okno, text="TotalSTL").pack()
    ttk.Label(okno, text="version: 0.0.1").pack()
    ttk.Label(okno, text="Author: Piotr Pawlik").pack()
    ttk.Label(okno, text="Jest to oprogramowanie pozwalajace na wyswietlanie plikow .STL, zarządzanie nimi i przeglądanie plikow .GCODE dla drukarek 3D").pack()
    ttk.Button(okno, text="EXIT", command=exit).pack()


        
ttk.Button(window, text="TotalSTL ver.0.0.1", command=button_clicked).pack()
ttk.Button(window, text="EXIT", command=exit).pack()


window.mainloop()