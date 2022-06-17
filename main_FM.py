from argparse import FileType
from distutils import filelist
from tabnanny import filename_only
from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import tkinter as tk
import os
import shutil
from win32com.client import Dispatch
from tkinter.filedialog import askopenfilename


def open_folder():
   folder = fd.askdirectory(title="Wybierz folder do otwarcia")
   
  
#win = tk.Tk()
def LIST_F_1():
    flist = fd.askdirectory(title='Wybierz folder do otwarcia')
    flist = os.listdir(flist)
    
    
    lbox = tk.Listbox(bg="#A9E7AF")
    lbox.pack()
    lbox.place(x=69, y=95, height=361, width=340)
    
    for item in flist:
        lbox.insert(tk.END, item)
        
        def opensystem(event):
            x = lbox.curselection()[0]
            #file = lbox.get(x)
            #with open(file) as file:
                #file = file.read()
            #text.delete('1.0', tk.END)
            #text.insert(tk.END, file)
                
        #text = tk.Text(win, bg='cyan')
        #text.pack()
        #def selected():
            #x = lbox.curselection()#[0]
            
            
    lbox.bind("<Double-Button-1>", opensystem)
    #lbox.bind("<<ListboxSelect>>", selected)
 
       
def LIST_F_2():
    flist2 = fd.askdirectory(title="Wybierz folder do otwarcia")
    flist2 = os.listdir(flist2)
    
    
    lbox = tk.Listbox(bg="#A9E7AF")
    lbox.pack()
    lbox.place(x=535, y=90, height=361, width=340)
    
    for item in flist2:
        lbox.insert(tk.END, item)
        
    def opensystem(event):
        x = lbox.curselection()[0]
        os.system(lbox.get(x))
    
    lbox.bind("<Double-Button-1>", opensystem)
    
#def delete_file():
   #os.remove(os.path.abspath(x))
   #mb.showinfo(title='Ukonczono', message='Plik usuniety!')