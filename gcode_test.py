import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

# Wyświetlenie okna dialogowego i wybór pliku GCode
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# Wczytanie pliku GCode
with open(file_path, 'r') as f:
    lines = f.readlines()

# Przetworzenie linii GCode i wyodrębnienie informacji o współrzędnych
x = []
y = []
for line in lines:
    if line.startswith('G1'):
        tokens = line.split(' ')
        for token in tokens:
            if token.startswith('X'):
                x.append(float(token[1:]))
            elif token.startswith('Y'):
                y.append(float(token[1:]))

# Wygenerowanie wykresu
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_aspect('equal')
ax.invert_yaxis()
plt.show()
