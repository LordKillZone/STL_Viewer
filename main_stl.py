#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy
import mpl_toolkits
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

#your_mesh = mesh.Mesh.from_file('cube.stl')

figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

your_mesh = mesh.Mesh.from_file('C:/PY_files/numpy_stl/cube.stl')
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

scale = your_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

pyplot.show()