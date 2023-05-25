import pyvista as pv
from tkinter import Tk, messagebox
from tkinter.filedialog import askopenfilename
from values import Values


def STL_view():
    try:
        Tk().withdraw()
        if Values.path == "":
            filename = askopenfilename()  # wybór pliku .stl do wczytania do wyświetlacza

            # Load the STL file
            your_mesh = pv.read(filename)

            # Create a plotter object and add the mesh to it
            plotter = pv.Plotter()
            plotter.add_mesh(your_mesh)
            plotter.add_axes()
            plotter.add_floor()
            plotter.enable_anti_aliasing()
            plotter.add_title(Values.name, font_size=12, color='red')

            # Set the background color and show the plot
            plotter.set_background("white")
            plotter.show()
            plotter.close()
            plotter.deep_clean()

        if len(Values.path) > 1:
            your_mesh = pv.read(Values.path)

            # Create a plotter object and add the mesh to it
            plotter = pv.Plotter()
            plotter.add_mesh(your_mesh)
            plotter.add_axes()
            plotter.add_floor()
            plotter.enable_anti_aliasing()
            plotter.add_title(Values.name, font_size=12, color='red')

            # Set the background color and show the plot
            plotter.set_background("white")
            plotter.show()
            plotter.close()
            plotter.deep_clean()

    except Exception as e:
        error_message = "Wystąpił błąd. Czy na pewno wybrałeś poprawny plik? " + str(e)
        messagebox.showerror("Error", error_message)

