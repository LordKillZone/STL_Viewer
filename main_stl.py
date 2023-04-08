#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

from tkinter import Tk
from tkinter.filedialog import askopenfilename


def STL_view():
    Tk().withdraw() 
    filename = askopenfilename()            #wybierniepliku .stl do wgrani do wyswietlacza

    figure = pyplot.figure()
    #figure.set_dpi(150)
    axes = figure.add_subplot(projection='3d')

    # Load the STL files and add the vectors to the plot
    your_mesh = mesh.Mesh.from_file(filename)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
    axes.collections[0].set_facecolor((1, 0.5, 0.6, 1))

    # Auto scale to the mesh size
    scale = your_mesh.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)
    axes.set_aspect('equal')

    # Show the plot to the screen
    pyplot.tight_layout()
    from mpl_toolkits.mplot3d import Axes3D
    axes = Axes3D(figure)

    pyplot.show()