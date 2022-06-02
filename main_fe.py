#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('TotalSTL')
window.geometry('1000x800+50+50')
window.iconbitmap('icon.ico')
ttk.Label(window, text="Testowanie tego mordo").pack()

window.mainloop()