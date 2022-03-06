import tkinter as tk
from tkinter.messagebox import *

master = tk.Tk()


def funcion_error():
    showerror("Titulo de mensaje de error", "Contenido de mensaje")


def funcion_show():
    if askyesno("Titulo de la consulta de verificacion", "Contenido de la consulta"):
        showinfo("Si", "Mensaje de informacion")
    else:
        showinfo("No", "Esta a punto de salir")


boton_error = tk.Button(master, text="Error", command=funcion_error)
boton_error.grid(row=2, column=1)

boton_show = tk.Button(master, text="Show", command=funcion_show)
boton_show.grid(row=3, column=1)

master.mainloop()
