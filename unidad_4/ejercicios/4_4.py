# Crear una función lambda que tome como parámetro una frase y la escriba al revés.

voltear_frase = lambda frase: frase[::-1]

frase = input("Escribi una frase: ")

print("La frase al reves es: ", voltear_frase(frase))
