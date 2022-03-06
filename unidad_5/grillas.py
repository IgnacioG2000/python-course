import tkinter as tk

master = tk.Tk()

el_id = tk.Label(master, text="id")
el_id.grid(row=0, column=0)

nombre = tk.Label(master, text="nombre")
nombre.grid(row=1, column=0)

entry_id = tk.Entry(master)
entry_id.grid(row=0, column=1)
entry_nombre = tk.Entry(master)
entry_nombre.grid(row=1, column=1)


def funcion():
    print("Se guardo el nombre")


boton_guardar = tk.Button(master, text="Guardar", command=funcion)
boton_guardar.grid(row=2, column=1)


master.mainloop()
