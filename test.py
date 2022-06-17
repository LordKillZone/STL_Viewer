from tkinter import *
import tkinter.messagebox as box
import tkinter.filedialog as fd
import os
import tkinter.messagebox as mb
import tkinter

window = Tk()
window.geometry("400x500")
window.title( 'Select File' )

frame = Frame( window )

# ---------------------------------

import time
from os import listdir
from os.path import isfile, join
mypath=fd.askdirectory(title='Wybierz folder do otwarcia')
lblText = StringVar()
lbl = Label( frame, textvariable=lblText)

fileList = [f for f in listdir(mypath) if isfile(join(mypath, f))]
fileList.sort()

# Methods -------------------------------------------------

def selectTextSearch():
    txt = lblText.get()
    if len(txt)> 0 and len(fileList) > 1:
        elem = 'is'
        pos = -1
        # Iterate over list items by index pos
        for i in range(len(fileList)):
            # Check if items matches the given element
            fileLetters = ''
            item = (fileList[i])
            if len(item) >= len(txt):
                substring = item[:len(txt)]
                
                if substring.lower() == txt.lower():
                    pos = i
                    break
        # If found
        if pos > -1:
            print(f'Index of element "{elem}" in the list is: ', pos)
            listbox.select_clear(0, "end")
            listbox.selection_set(pos)
            listbox.see(pos)
            listbox.activate(pos)
            listbox.selection_anchor(pos)

def dialog():
    box.showinfo( 'Selection' , 'Your Choice: ' + \
    listbox.get( listbox.curselection() ) )

def from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb  

def quit(self):
    window.destroy()
    
def delete():
    os.remove(mypath/selection)
    mb.showinfo(title='Ukonczono', message='Plik usuniety!')

# EVENTS --------------------------------------------------


def actionDel(self, event):
        try:
            selection = self.listRegisteredSpecies.selection_get()
            selectionSplit = selection.split(": ")
            self.parent.optimizer.speciesList.remove((selectionSplit[0], selectionSplit[1]))
            self.gui.event_generate("<<Update>>")
        except tkinter.TclError:
            # no selection
            pass

def listboxSelection(event):
    widget = event.widget
    selection=widget.curselection()
    picked = widget.get(selection[0])
    print(picked)
    actionDel()
    


def keyPress(event):
    
    azList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9','_','.','-']
    charPressed = (event.char).lower()
    if charPressed in azList:
        print("pressed", charPressed)
        txt = lblText.get()
        txt += charPressed
        lblText.set(txt)
        selectTextSearch()

def backspacePress(event):
    print("backspacePress")
    txt = lblText.get()
    if len(txt)> 0:
        # remove last character
        txt = txt[:-1]
        lblText.set(txt)
        selectTextSearch()

# GUI SETUP --------------------------------------------------

listbox = Listbox(frame)
for name in fileList:
    listbox.insert('end', name)
listbox.focus()
listbox.selection_set(0,0)
# listbox.bind('<<ListboxSelect>>',CurSelet)
listbox.bind('<Return>',listboxSelection)
listbox.bind('<Button-1>',listboxSelection)
# listbox.bind('<Space>',CurSelet)
listbox.bind('<Tab>',listboxSelection)
listbox.bind('<Key>',keyPress)
listbox.bind('<BackSpace>',backspacePress)
listbox.bind('<Escape>',quit)
# listbox.bind('<Return>',CurSelet)


lbl.pack()
listbox.pack( side = LEFT )
frame.pack( padx = 0, pady = 0 )


# THEME ----------------------------------------------
colorBg=from_rgb((60,60,60))
listboxSelectionBg=from_rgb((73,141,255))
frame.configure(background=colorBg)
lbl.configure(background=colorBg, foreground="white")
listbox.config(width=400,height=450)
listbox.config(
    background=colorBg, 
    selectbackground=listboxSelectionBg,
    selectforeground="white",
    foreground="white",
    borderwidth=0,
     bd= 0
    )



window.mainloop()