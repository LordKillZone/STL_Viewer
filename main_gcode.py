import os

import texteditor
import tkinter.filedialog as fd
from tkinter.filedialog import askopenfilename



def GCODE():
    file = fd.askopenfilename(title="Wybierz folder do otwarcia")
    command = print('dziala')
    # f = open("file.gcode", "r")
    # print(f.read())
    # f.close()
    os.startfile(file)

def gCODE2(file2):
    os.startfile(file2)
# import gcodeparser
# import numpy as np
# import pythreejs as three
#
# # Wczytaj plik G-code
# with open('test.gcode', 'r') as f:
#     gcode_data = f.read()
#
# # Przetwórz plik G-code i wyodrębnij współrzędne punktów
# parser = gcodeparser.GcodeParser(gcode_data)
# x, y, z = [], [], []
# for cmd in parser.get_commands():
#     if cmd['cmd'] == 'G1':
#         x.append(cmd['params']['X'])
#         y.append(cmd['params']['Y'])
#         z.append(cmd['params']['Z'])
#
# # Utwórz geometrię z punktów
# points_geometry = three.BufferGeometry(
#     attributes={
#         'position': three.BufferAttribute(np.array([x, y, z]).T, normalized=False),
#     }
# )
#
# # Utwórz materiał punktów
# points_material = three.PointsMaterial(
#     color='blue',
#     size=0.05,
# )
#
# # Utwórz punkty
# points = three.Points(
#     geometry=points_geometry,
#     material=points_material,
# )
#
# # Wyświetl punkty
# renderer = three.Renderer()
# camera = three.PerspectiveCamera(position=[0, 0, 10], aspect=1)
# scene = three.Scene(children=[points])
# controller = three.OrbitControls(controlling=camera)
# display(three.Renderer(camera=camera, scene=scene, controls=[controller]))
