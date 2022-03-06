import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import askcolor

master = tk.Tk()


def funcion_guardar():
    ruta = askopenfilename()
    print(ruta)
    resultado = askcolor(color="#00ff00", title="El titulo")
    print(resultado)
    print(resultado[1])


boton_guardar = tk.Button(master, text="Guardar", command=funcion_guardar)
boton_guardar.grid(row=2, column=1)


master.mainloop()
