from tkinter import *
import math
from tkinter.messagebox import *


main = Tk()

main.title("Formula Resolvente")
main.geometry("400x200")

a = IntVar()
b = IntVar()
c = IntVar()
x1 = IntVar()
x2 = IntVar()


def calcular_raices():
    discriminante = b.get() ** 2 - 4 * a.get() * c.get()

    if discriminante > 0:
        raiz1 = (-b.get() + math.sqrt(discriminante)) / 2 * a.get()
        raiz2 = (-b.get() - math.sqrt(discriminante)) / 2 * a.get()
        round(raiz1, 3)
        round(raiz2, 3)
    elif discriminante == 0:
        raiz1 = -b.get() / 2 * a.get()
        raiz2 = raiz1
        round(raiz1, 3)
        round(raiz2, 3)

    x1.set(raiz1)
    x2.set(raiz2)
    print(str(x1.get()))
    showinfo("Raiz 1", str(x1.get()))
    showinfo("Raiz 2", str(x2.get()))


coef_a = Label(main, text="Ingrese el coeficiente a")
coef_a.grid(row=0, column=0)

coef_b = Label(main, text="Ingrese el coeficiente b")
coef_b.grid(row=1, column=0)

coef_c = Label(main, text="Ingrese el coeficiente c")
coef_c.grid(row=2, column=0)


entry_coef_a = Entry(main, textvariable=a, width=15)
entry_coef_a.grid(row=0, column=1)

entry_coef_b = Entry(main, textvariable=b, width=15)
entry_coef_b.grid(row=1, column=1)

entry_coef_c = Entry(main, textvariable=c, width=15)
entry_coef_c.grid(row=2, column=1)

boton_resolver = Button(
    main,
    text="Calcular raices x1 y x2",
    command=calcular_raices,
)
boton_resolver.grid(row=3, column=0)

main.mainloop()
