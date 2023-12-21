# Crear dos tuplas de manera tradicional.

tupla1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tupla2 = 'andres', 42, 1.70, 'Colombiano', 1981     # Las podemos definir sin usar paréntesis.
tupla3 = ((1,2,3), (4,5,6), (7,8,9))
tupla4 = (['a','b','c'], ['d','e','f'], ['g','h','i'])

# Acceder a uno y a varios valores dentro de las tuplas.
print("Tupla 2 en la posición 3: ",tupla2[3],"\n"
      "Tupla 1 en las posiciones (2,5): ",tupla1[2:6])

# Las tuplas no permiten modificar los elementos, excepto cuando el elemento está dentro de una lista.
# tupla2[0] = "Felipe"
tupla4[1][1] = 'E'

print("Tupla 1, posiciones 5 a 9: ",tupla1[5:])
print("Posición (2,2) de la tupla 3: ",tupla3[2][2])
print("Tupla 4: ",tupla4)

# Iterar sobre uan tupla.
for i in range(len(tupla2)):        # Usando la función range, indicando el límite superior a través del tamaño de la tupla.
      print(tupla2[i], end=" ")

print("\n")                         # Usando el valor que se almacena en j en cada una de las iteraciones.
for j in tupla1:
      print(j, end=" ")



