from distutils import filelist
from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import tkinter as tk
import os
import shutil


def open_folder():
   folder = fd.askdirectory(title="Select Folder to open")
   
def delete_file():
   file = fd.askopenfilename(title='Choose a file to delete', filetypes=[("All files", "*.*")])
   os.remove(os.path.abspath(file))
   mb.showinfo(title='Ukonczono', message='Plik usuniety!')
   
def LIST_F_1():
    flist = fd.askdirectory(title="Select Folder to open")
    flist = os.listdir(flist)
    
    
    lbox = tk.Listbox(bg="#A9E7AF")
    lbox.pack()
    lbox.place(x=69, y=95, height=361, width=340)
    
    for item in flist:
        lbox.insert(tk.END, item)
        
def LIST_F_2():
    flist2 = fd.askdirectory(title="Select Folder to open")
    flist2 = os.listdir(flist2)
    
    
    lbox = tk.Listbox(bg="#A9E7AF")
    lbox.pack()
    lbox.place(x=535, y=90, height=361, width=340)
    
    for item in flist2:
        lbox.insert(tk.END, item)