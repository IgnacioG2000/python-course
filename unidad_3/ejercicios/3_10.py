"""
Escriba un programa que guarde en una variable una contraseña y consulte al
usuario por la contraseña hasta que esta sea correcta. 
El programa debe informar al usuario si la contraseña fue correcta o no.
"""

contrasenia_usuario = "NachoAyudante2000"

intento_contrasenia = input("Digita contraseña: ")

while contrasenia_usuario != intento_contrasenia:
    intento_contrasenia = input("Contraseña incorrecta. Intenta nuevamente: ")

print("La contraseña es correcta")
