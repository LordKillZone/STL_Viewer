from argparse import FileType
from distutils import filelist
from tabnanny import filename_only
from tkinter import *
import shutil
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import tkinter as tk
import os
from values import Values
import glob
import shutil
#from win32com.client import Dispatch
from tkinter.filedialog import askopenfilename

import main_stl_faster


def open_folder():
   folder = fd.askdirectory(title="Wybierz folder do otwarcia")
   folder2 = fd.askdirectory(title="Wybierz folder do otwarcia")
   
  
#win = tk.Tk()
def LIST_F_1():
    folder = fd.askdirectory(title='Wybierz folder do otwarcia')
    flist = glob.glob(os.path.join(folder, '*.stl'))

    lbox = tk.Listbox(bg="#A9E7AF")
    lbox.pack()
    lbox.place(x=69, y=95, height=361, width=340)

    for item in flist:
        filename = os.path.basename(item)
        lbox.insert(tk.END, filename)

    def opensystem(event):
        selection = lbox.curselection()
        if selection:
            index = selection[0]
            filename = os.path.join(folder, flist[index])
            Values.path = filename
            Values.p_left = filename
            print("Wybrano plik:", Values.path)
            main_stl_faster.STL_view()

    def opensystem_click(event):
        selection = lbox.curselection()
        if selection:
            index = selection[0]
            filename = os.path.join(folder, flist[index])
            Values.l_right = filename
            print("Wybrano plik:", Values.l_right)

    lbox.bind("<Double-Button-1>", opensystem)
    lbox.bind("Button-1", opensystem_click)
 
       
def LIST_F_2():
    folder2 = fd.askdirectory(title="Wybierz folder do otwarcia")
    #flist2 = os.listdir(flist2)
    flist2 = glob.glob(os.path.join(folder2, '*.stl'))
    
    
    lbox = tk.Listbox(bg="#A9E7AF")
    lbox.pack()
    lbox.place(x=535, y=90, height=361, width=340)
    
    for item in flist2:
        filename = os.path.basename(item)
        lbox.insert(tk.END, filename)

        
    def opensystem(event):
        selection = lbox.curselection()
        if selection:
            index = selection[0]
            filename = os.path.join(folder2, flist2[index])
            Values.path = filename
            Values.p_right = filename
            print("Wybrano plik:", Values.path)
            main_stl_faster.STL_view()

    def opensystem_click(event):
        selection = lbox.curselection()
        if selection:
            index = selection[0]
            filename = os.path.join(folder2, flist2[index])
            Values.p_right = filename
            print("Wybrano plik:", Values.p_right)
    
    lbox.bind("<Double-Button-1>", opensystem)
    lbox.bind("Button-1", opensystem_click)


def COPY_LtoR():

    if (len(Values.p_left)>1):
        shutil.copyfile(Values.p_left, Values.p_right)

    else:
        print("lewa: " + Values.p_left)
        print("prawa: " + Values.p_right)

#def delete_file():
   #os.remove(os.path.abspath(x))
   #mb.showinfo(title='Ukonczono', message='Plik usuniety!')