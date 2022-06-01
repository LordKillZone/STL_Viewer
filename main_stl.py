#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from importlib.resources import path
import numpy
import mpl_toolkits
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() 
filename = askopenfilename()



figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

your_mesh = mesh.Mesh.from_file(filename)
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

scale = your_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

pyplot.show()