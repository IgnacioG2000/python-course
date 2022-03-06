import tkinter as tk

master = tk.Tk()


def hola():
    print("Hola")


menubar = tk.Menu(master)

menu_archivo = tk.Menu(menubar, tearoff=0)
menu_archivo.add_command(label="Abrir", command=hola)
menu_archivo.add_command(label="Guardar", command=hola)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=master.quit)
menubar.add_cascade(label="Archivo", menu=menu_archivo)

menu_edicion = tk.Menu(menubar, tearoff=0)
menu_edicion.add_command(label="Abrir", command=hola)
menu_edicion.add_command(label="Guardar", command=hola)
menu_edicion.add_separator()
menu_edicion.add_command(label="Salir", command=master.quit)
menubar.add_cascade(label="Editar", menu=menu_edicion)

submenu = tk.Menu(menu_edicion, tearoff=True)
submenu.add_command(label="Editar color", command=hola)
submenu.add_command(label="Guardar", command=hola)
menu_edicion.add_cascade(label="Otros", menu=submenu)

master.config(menu=menubar)
master.mainloop()
