from math import *
from random import randint
from numpy import *

# Crear una lista de la manera tradicional.

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]                    # Vector de 9 elementos.
lista2 = ['andres', 42, 1.70, 'colombiano', 1981]
lista3 = [[0,1,2], [3,4,5], [6,7,8], [9,0,1]]           # Matriz de 4 x 3


# Acceder a uno o varios valores de las listas.
print("Lista 1 en la posición 4: ",lista1[4],"\n"
      "Lista 3, fila 1: ",lista3[1], "\n"
      "Lista 1, posiciones 3 a 6: ",lista1[3:7], "\n"
      "Lista 3 en la posición (2,3): ",lista3[2][2])    # El número de listas indica el número de filas.
                                                        # El número de elementos de cada lista indica el número de columnas.
                                                        # Todas las listas deben tener el mismo número de elementos.

print("Lista 2 en las posiciones 1 a 4: ",lista2[1:])

# Invertir el orden de una lista.
print("Lista 1 invertida: ",lista1[::-1])


# Modificar un elemento dentro de las listas.
lista2[3] = 'Paisa'
print("Lista 2 modificada en la posición 3: ",lista2)
lista3[1][2] = 5.5
print("Lista 3 modificada en la posición (1,2): ",lista3)


# Recorrer una lista.
for i in lista3:
      print(i)


"""Métodos de la clase list."""

# Si queremos saber el tamaño de una lista.
tamañoLista1 = len(lista1)
print("Tamaño de la lista 1: ", tamañoLista1)


# Agregar un elemento nuevo a la lista.
lista3.append([2,3,4])
print("Lista 3 con una fila agregada: ",lista3)
# El opeardor + o de concatenación es una alternativa al método append.


# Eliminar el último elemento de una lista.
lista2.pop()
print("Lista 2 luego de eliminar el 1981: ",lista2)


# Insertar un nuevo elemento en la lista 1.
lista1.insert(2, 2.5)
print(lista1)


# Eliminar un elemento de cualquier posición.
lista2.remove(42)
print("Lista 2 luego de eliminar el 42: ",lista2)


# Eliminar un elemento usando su indice.
del lista1[2]
print("Lista 1 sin el tercer elemento: ",lista1)


# Contar el número de veces que aparece un elemento en una lista.
conteo = lista1.count(5)
print("El número 5 aparece: ",conteo, " veces.")


# Consultar la posición en la que se encuentra un elemento:
posicion = lista2.index('andres')
print("andres se encuentra en la posición ",posicion," de la lista 2.")


# Ordenar una lista de manera ascendente y descendente.
lista4 = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
lista4.sort()
print("Lista 4 ordenada de manera ascendente: ",lista4)
lista4.reverse()
print("Lista 4 ordenada de manera descendente: ",lista4)

lista6 = ['español', 'matemáticas', 'química', 'física']
lista6.sort()
print("Lista 6 ordenada: ",lista6)                          # No se pueden ordenar listas con tipos de datos diferentes.

lista7 = [[3, 4], [1, 5], [7, 8], [5, 7], [2, 6]]
lista7.sort()
print("Lista 7 ordenada: ",lista7)                          # Los ordena con respecto al primer elemento.


# Clear lo usamos para vaciar la lista.
lista5 = ['a', 'b', 'c']
lista5.clear()
print("Lista 5 vacia: ",lista5)


# Saber si un elemento hace parte de una lista.
pertenece = 1 in lista4
print(pertenece)


# Comparar dos listas usando un operador relacional.
print(lista1, "\n",
      lista4, "\n",
      lista1 < lista4)


# Para reproducir o duplicar una lista.
print("Lista 2 duplicada: ",2 * lista2)


# Para formar parejas con los elementos de una lista.
pares = zip(lista1, lista4)
lista8 = list(pares)                      # Generamos una lista de esas parejas.
print(lista8)


# Forma alterna de iterar sobre una lista.
for i,j in lista8:
      print(i,j, end=" ")


# Generar una lista por mapeo.
def cubo(x):
      return pow(x, 3)

cubos = map(cubo, range(5))               # Función que recibe como parámetros una función mas un rango de valores.
lista9 = list(cubos)                      # Generar una lista a partir de dichos resultados.
print("\n")
print(lista9)


# Generar una lista a traves de un filtro.
def pares(x):
      if x % 2 == 0:
            return x

pares = filter(pares, range(11))     # Función que recibe como parámetros una función de filtro y un rnago de valores.
lista10 = list(pares)
print("Lista 10: ",lista10)


# Crear listas mediante declaraciones implicitas.
var1 = range(11)                    # Almacenar en la variable los valores entre 0 y 10.
lista11 = list(var1)
print("Lista 11: ",lista11)

var2 = [i for i in range(11)]       # Cuando hacemos uso del ciclo for, no necesitamos las iteraciones de la función list
print("Variable 2: ",var2)


var3 = [[i] for i in range(11)]
print("variable 3: ",var3)


var4 = range(11)
lista12 = [t for t in var4 if (t % 2 == 0)]     # Usamos una estructura condicional sin necesidad de una función.
print(lista12)


lista13 = [randint(0, 10) for t in range(11)]
print("Lista 13: ",lista13)


# Crear listas mediante declaraciones explicitas.
lista14 = [ ]
lista15 = [ ]

# Agregamos valores a la lista 14.
for i in range (11):
      lista14.append(i)

for j in range (11):
      lista15.append([j])

print("Lista 14: ",lista14)
print("Lista 15: ",lista15)

# Podemos usar el operador + en lugar de append para agregar elementos a las listas. Su funcionamiento es igual.
# lista14 + [i]
# lista15 + [[i]]


# Concatenar dos listas.
concatenacion = var2 + lista11
print("Concatenación = ",concatenacion)


# Para generar una copia de una lista.
lista16 = lista10.copy()
print("Lista 16 (copia de la lista 10): ",lista16)


# Para hallar el máximo valor de una lista.
maximo = max(lista4)
print("Máximo valor de la lista 4: ",maximo)


# Para hallar el valor mínimo de una lista.
minimo = min(lista4)
print("Máximo valor de la lista 4: ",minimo)


# Para sumar los elementos numéricos de una lista.
suma = sum(lista4)
print("Suma de valores de la lista 4 = ", suma)


# Para prevenir errores al usar algunas funciones, podemos usar el operador de inclusión para hacer validaciones.
# if 8 in lista4:
#     lista4.remove(8)

# Los métodos se pueden aplicar a listas con diferente tipo de elementos.


# Funciones de Numpy para arreglos de una y dos dimensiones:
vector1 = array(lista4)                                                 # Creamos un vector a partir de una lista.
print("Producto de los elementos de la lista 4: ",prod(vector1))        # Producto de los elementos del vector1.
print("Posición del mayor valor de la lista 4: ",argmax(vector1))       # Posición del valor mayor.
print("Posición del menor valor de la lista 4: ",argmin(vector1))       # Posición del menor valor.
print("Media aritmética de los valores de la lista 4: ", mean(vector1)) # Promedio de los elementos de la lista 4.
print("Desviación standar de los valores de la lista 4: ",format(std(vector1), ".3f")) #Desviación standar.

x1 = [1/3, 1/5, 1/7, 1/9]
print([float('%6.4f' % x1[i]) for i in range(len(x1))])








