import tkinter as tk
from tkinter import ttk

mi_id = 0

master = tk.Tk()

var_nombre = tk.StringVar()
var_apellido = tk.StringVar()

nombre = tk.Label(master, text="Nombre")
nombre.grid(row=0, column=0)


def funcion_guardar():
    global mi_id
    mi_id += 1
    tree.insert(
        "", "end", text=str(mi_id), values=(var_nombre.get(), var_apellido.get())
    )


def funcion_borrar():
    global mi_id
    item = tree.focus()
    print(item)
    print(tree.item(item))
    tree.delete(item)
    mi_id -= 1


apellido = tk.Label(master, text="Apellido")
apellido.grid(row=1, column=0)

entry_nombre = tk.Entry(master, textvariable=var_nombre, width=25)
entry_nombre.grid(row=0, column=1)
entry_apellido = tk.Entry(master, textvariable=var_apellido, width=25)
entry_apellido.grid(row=1, column=1)

tree = ttk.Treeview(master)
tree["columns"] = ("col1", "col2")
tree.column("#0", width=50, minwidth=50)
tree.column("col1", width=80, minwidth=80)
tree.column("col2", width=80, minwidth=80)

tree.grid(column=0, row=4, columnspan=4)

boton_guardar = tk.Button(master, text="Guardar", command=funcion_guardar)
boton_guardar.grid(row=2, column=1)

boton_borrar = tk.Button(master, text="Borrar", command=funcion_borrar)
boton_borrar.grid(row=3, column=1)


master.mainloop()
