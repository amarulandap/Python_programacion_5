# Crear un string.

cadena1 = "programa de python"

print("Cadena 1 en la poisición 8: ",cadena1[8])
print("Cadena 1 en la posición 4: ",cadena1[4])
print("Cadena 1, posiciones (2, 5): ",cadena1[2:6])

# Los Strings no se pueden modificar con asignaciones a los indices:
# cadena1[3] = Y

digitos = digits
print("Digitos: ",digits,"\n",
      "Ascii: ",ascii_letters,"\n",
      "Minúsculas: ",ascii_lowercase,"\n",
      "Mayúsculas: ",ascii_uppercase,"\n",
      "Hexadecimales: ",hexdigits)

# Convertir la primera letra de la cadena en mayúscula.
cadena2 = "convertir la primera letra en mayúscula."
print(cadena2, " - ", cadena2.capitalize())

# Cadena centrada en N espacios.
cadena3 = "cadena centrada."
print(cadena3, " - ", cadena3.center(6, 'X'))

# Contar el número de ocurrencias de una subcadena.
print('Número de veces que se repite la letra p en ',cadena1, ':', cadena1.count('p'))

# Buscar si un caracter se encuentra en una cadena.
cadena4 = "Uno de los grandes males de la humanidad es la indiferencia que manifiestan algunas personas."
pertenece = cadena4.find('buenos')
if pertenece == -1:
    print("Buenos no pertenece a la cadena 4.")
else:
    print("Buenos pertenece a la cadena 4.")

if 'males' in cadena4:
    print("males pertenece a la cadena 4.")
else:
    print("males pertenece a la cadena 4.")

# Saber si todos los caracteres son alfabéticos.
alfabeticos = cadena4.isalpha()
if alfabeticos:
    print("Todos los caracteres son alafabéticos.")
else:
    print("hay caracteres que no son alfabéticos.")

# Mayor indice de una subcadena.
print("La palabra indiferencia se encuentra a partir de la posición: ", cadena4.rfind('indiferencia'))

# Saber si todos los caracteres son dígitos.
cadena5 = "123456789"
digitos = cadena5.isdigit()
if digitos:
    print("Todos los caracteres son dígitos.")
else:
    print("No todos los caracteres son dígitos.")

# Saber si todos los caracteres son minúsculas.
minusculas = cadena1.islower()
if minusculas:
    print("Todos los caracteres son minúsculas.")
else:
    print("No todos los caracteres son minúsculas.")

# Saber si todos los caracteres son mayúsculas.
mayusculas = cadena2.isupper()
if mayusculas:
    print("Todos los caracteres son mayúsculas.")
else:
    print("No todos los caracteres son mayúsculas.")

# Justificar una cadena a la izquierda.
cadena6 = "   Cadena justificada a la izquierda 3 espacios.   "
print(cadena6.ljust(3))

# Justificar a la derecha una cadena.
print(cadena6.rjust(3))

# Eliminar espacios a la izquierda de la cadena.
print(cadena6.lstrip())

# Eliminar los espacios a la derecha de la cadena.
print(cadena6.rstrip())

print(cadena6.strip())

# Reemplazar una parte de la cadena 6.
print(cadena6.replace('Cadena', 'String'))

# Convertir una cadena a minúsculas.
cadena7 = "CADENA CONVERTIDA A MINÚSCULAS."
print(cadena7.lower())

# Convertir una cadena a mayúsculas.
print("Cadena 1 convertida a mayúsculas: ",cadena1.upper())

# Generar una lista a partir de una cadena de caracteres.
print("Lista de palabras: ",cadena7.split())

# Generar una lista de letras.
lista1 = list(cadena7)
print("Cadena convertida en lista: ",lista1)

print(','.join(cadena7))

# Saber la longitud de la cadena.
print("La longitud de la cadena 4 es: ",len(cadena4))

# Concatenar dos cadenas.
print("cadena 1 y cadena 5 concatenadas: ", cadena1 + cadena5)



