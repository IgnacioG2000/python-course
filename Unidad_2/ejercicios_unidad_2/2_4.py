# Realice un programa que consulte la edad y en caso de que el valor ingresado
# supere la fecha de jubilación, presente en la terminal el
# mensaje “Ya está en edad de jubilarse",
# en caso contrario que presente "Aún está en edad de trabajar”

edad = int(input("Edad: "))

if edad >= 65 and edad <= 100:
    print("Ya esta en edad para jubilarse")
else:
    print("Aun esta en edad de trabajar")
