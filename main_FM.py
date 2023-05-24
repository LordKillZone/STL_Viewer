from argparse import FileType
from distutils import filelist
from tabnanny import filename_only
from tkinter import *
import shutil
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import tkinter as tk
import os
from tkinter import messagebox

from values import Values
import glob
import shutil
# from win32com.client import Dispatch
from tkinter.filedialog import askopenfilename

import main_stl_faster


def open_folder1():
    Values.folder = fd.askdirectory(title="Wybierz folder do otwarcia")
    LIST_F_1()


def open_folder2():
    Values.folder2 = fd.askdirectory(title="Wybierz folder do otwarcia")
    LIST_F_2()


# win = tk.Tk()
def LIST_F_1():
    # Values.folder = fd.askdirectory(title='Wybierz folder do otwarcia')
    if len(Values.folder) == 0:
        messagebox.showerror("Error", "Proszę wybrać folder do otwarcia")
    else:
        flist = glob.glob(os.path.join(Values.folder, '*.stl'))

        lbox = tk.Listbox(bg="#A9E7AF")
        lbox.pack()
        lbox.place(x=69, y=95, height=361, width=340)

        Values.p_right = Values.folder
        for item in flist:
            filename = os.path.basename(item)
            lbox.insert(tk.END, filename)

        def opensystem(event):
            selection = lbox.curselection()
            if selection:
                index = selection[0]
                filename = os.path.join(Values.folder, flist[index])
                Values.path = filename
                Values.p_left = filename
                print("Wybrano plik lewa:", Values.path)
                print("folder = " + Values.p_right)
                main_stl_faster.STL_view()

    def opensystem_click(event):
        selection = lbox.curselection()
        if selection:
            index = selection[0]
            filename = os.path.join(Values.folder, flist[index])
            Values.p_left = filename
            print("Wybrano plik lewy:", Values.p_left)
            print("folder lewy: " + Values.folder)

    lbox.bind("<Double-Button-1>", opensystem)
    lbox.bind("<ButtonRelease-1>", opensystem_click)


def LIST_F_2():
    if len(Values.folder2) == 0:
        messagebox.showerror("Error", "Proszę wybrać folder do otwarcia")
    # Values.folder2 = fd.askdirectory(title="Wybierz folder do otwarcia")
    # flist2 = os.listdir(flist2)
    else:
        flist2 = glob.glob(os.path.join(Values.folder2, '*.stl'))
        Values.p_left = Values.folder2

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
                filename = os.path.join(Values.folder2, flist2[index])
                Values.path = filename
                Values.p_right = filename
                print("Wybrano plik prawy:", Values.path)
                print("folder prawy: " + Values.folder2)
                main_stl_faster.STL_view()

        def opensystem_click(event):
            selection = lbox.curselection()
            if selection:
                index = selection[0]
                filename = os.path.join(Values.folder2, flist2[index])
                Values.p_right = filename
                print("Wybrano plik prawy:", Values.p_right)

        lbox.bind("<Double-Button-1>", opensystem)
        lbox.bind("<ButtonRelease-1>", opensystem_click)


def COPY_LtoR():
    # shutil.copy2("D:/DRUK 3D/STL/Spiral_Vase/Spiral_Vase1.STL", "D:/DRUK 3D/STL/Frankie")
    if len(Values.p_left) > 1 and len(Values.folder2) > 1:

        shutil.copy2(Values.p_left, Values.folder2)
        print("kopiuj: " + Values.p_left)
        print("do: " + Values.folder2)
        LIST_F_1()
        LIST_F_2()

    else:
        print("Nie skopiowano")
        if len(Values.p_left) == 0:
            messagebox.showerror("Error", "Proszę wybrać plik do skopiowania")
        if len(Values.folder2) == 0:
            messagebox.showerror("Error", "Proszę wybrać folder gdzie skopiować plik")


def COPY_RtoL():
    # shutil.copy2("D:/DRUK 3D/STL/Spiral_Vase/Spiral_Vase1.STL", "D:/DRUK 3D/STL/Frankie")
    if len(Values.p_right) > 1 and len(Values.folder) > 1:

        shutil.copy2(Values.p_right, Values.folder)
        print("kopiuj: " + Values.p_right)
        print("do: " + Values.folder)
        LIST_F_1()
        LIST_F_2()

    else:
        print("Nie skopiowano")
        if len(Values.p_right) == 0:
            messagebox.showerror("Error", "Proszę wybrać plik do skopiowania")
        if len(Values.folder) == 0:
            messagebox.showerror("Error", "Proszę wybrać folder gdzie skopiować plik")


def MOVE_LtoR():
    if len(Values.p_left) > 1 and len(Values.folder2) > 1:

        shutil.move(Values.p_left, Values.folder2)
        print("przenies: " + Values.p_left)
        print("do: " + Values.folder2)
        LIST_F_1()
        LIST_F_2()

    else:
        print("Nie przeniesiono")
        if len(Values.p_left) == 0:
            messagebox.showerror("Error", "Proszę wybrać plik do skopiowania")
        if len(Values.folder2) == 0:
            messagebox.showerror("Error", "Proszę wybrać folder gdzie skopiować plik")


def MOVE_RtoL():
    if len(Values.p_right) > 1 and len(Values.folder) > 1:

        shutil.move(Values.p_right, Values.folder)
        print("przenieś: " + Values.p_right)
        print("do: " + Values.folder)
        LIST_F_1()
        LIST_F_2()

    else:
        print("Nie przeniesiono")
        if len(Values.p_right) == 0:
            messagebox.showerror("Error", "Proszę wybrać plik do skopiowania")
        if len(Values.folder) == 0:
            messagebox.showerror("Error", "Proszę wybrać folder gdzie skopiować plik")


def remove_left():
    if len(Values.p_left) == 0:
        messagebox.showerror("Error", "Proszę wybrać plik do usunięcia")
    else:
        os.remove(Values.p_left)
        LIST_F_1()
        LIST_F_2()

def remove_right():
    if len(Values.p_right) == 0:
        messagebox.showerror("Error", "Proszę wybrać plik do usunięcia")
    else:
        os.remove(Values.p_right)
        LIST_F_1()
        LIST_F_2()
