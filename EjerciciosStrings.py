"""1. Programa para invertir el orden de los caracteres de una cadena."""

def invertirCadena(cadena):             # Recibe como parámetro la cadena a invertir.

    inversor = ''
    for i in cadena:                    # En cada iteración me concatena la letra con lo ya almacenado en inversor.
        inversor = i + inversor

    return inversor                     # Retorna la cadena ya invertida.


cadena = input("Ingrese una frase: ")
cadenaInvertida = invertirCadena(cadena)

print(cadena, "\n",
      cadenaInvertida)

"""2. Programa para determinar que una frase es un palíndromo."""

# solicitar el ingreso de la frase.
frase1 = input("\nIngrese una frase: ")
print(frase1)

# convertimos toda la frase a mayúsculas o a minúsculas.
frase1 = frase1.lower()

# Eliminamos todos los espacios en blanco.
frase1 = frase1.replace(' ','')

# Invertimos la frase.
fraseInvertida = invertirCadena(frase1)

if frase1 == fraseInvertida:
    print("Si es un palíndromo.")
else:
    print("No es un palíndromo.")


"""3. Programa para validar si una palabra pertenece a una frase."""

# Pedir al usuario que ingrese la frase.
frase2 = input("\nIngrese una frase: ")
print("Frase original: ",frase2)

# Contar el número de vocales que tiene la frase.
cantidadVocales = (frase2.count('a') + frase2.count('e') + frase2.count('i') + frase2.count('o') + frase2.count('u') +
                   frase2.count('á') + frase2.count('é') + frase2.count('í') + frase2.count('ó') + frase2.count('ú') +
                   frase2.count('A') + frase2.count('E') + frase2.count('I') + frase2.count('O') + frase2.count('U'))
print("Cantidad de vocales: ",cantidadVocales)

# Contar la cantidad de veces que la frase contiene una palabra.
palabra = input("\nIngrese la palabra a buscar: ")
print("Palabra a buscar: ",palabra)

cantidadPalabra = frase2.count(palabra)
print("La palabra",palabra, "se repite",cantidadPalabra, "veces.")





