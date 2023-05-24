import pyvista as pv
from tkinter import Tk, messagebox
from tkinter.filedialog import askopenfilename
from values import Values


def STL_view():
    try:
        Tk().withdraw()
        if (Values.path==""):
            filename = askopenfilename()  # wybierniepliku .stl do wgrani do wyswietlacza

            # Load the STL file
            your_mesh = pv.read(filename)

            # Create a plotter object and add the mesh to it
            plotter = pv.Plotter()
            plotter.add_mesh(your_mesh)

            # Set the background color and show the plot
            plotter.set_background("white")
            plotter.show()

        if len(Values.path)>1:
            your_mesh = pv.read(Values.path)

            # Create a plotter object and add the mesh to it
            plotter = pv.Plotter()
            plotter.add_mesh(your_mesh)

            # Set the background color and show the plot
            plotter.set_background("white")
            plotter.show()

    except Exception as e:
        error_message = "Wystąpił bład na pewno wybrałeś poprawny plik?" + str(e)
        messagebox.showerror("Error", error_message)


