#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def GCODE():
    
    Tk().withdraw() 
    filename_2 = askopenfilename()    #wybierniepliku do wgrania
    
    os.startfile(filename_2)