#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from importlib.resources import path
import numpy
import mpl_toolkits
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() 
filename = askopenfilename()            #wybierniepliku .stl do wgrani do wyswietlacza



figure = pyplot.figure()        #Tworzenie nowego plotu
axes = mplot3d.Axes3D(figure)

your_mesh = mesh.Mesh.from_file(filename)       #Otwarcie wybranego pliku .stl
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

scale = your_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)        #automatyczne przeskalowanie pliku

pyplot.show()       #otwarcie pliku w GUI podobny do MATLABA