from random import *
from ValidacionDatos import *
from math import *

"""Programa para validar los estudiantes que están inscritos en una o ambas materias."""

# 1. Crear la lista de los estudiantes de la materia A.
# 2. Crear la lista de los estudiantes de la materia B.
# 3. Recorrer la lista A comparando cada uno de sus elementos con todos los elementos de la lista B.
# 4. Crear una lista con los estudiantes matriculados en ambas materias.
# 5. Calcular el tamaño de la lista generada.
# 6. De la lista A eliminar los que están matriculados en ambas.

# Determinar el número de estudiantes de las materias.
totalEstudiantesA = ValidarEntero("Número de estudiantes materia A: ", "Error, ingrese un número entero.")
totalEstudiantesB = ValidarEntero("Número de estudiantes materia B: ","Error, ingrese un número entero." )

# Lista de estudiantes de la materia A.
estudiantesA = [ ]
for i in range(1, totalEstudiantesA + 1):
    estudiante = randint(1, 100)            # generamos un número de identificación aleatorio
    if estudiante not in estudiantesA:
        estudiantesA.append(estudiante)

estudiantesA.sort()

# Lista de estudiantes de la materia B.
estudiantesB = [ ]
for i in range(1, totalEstudiantesB + 1):
    estudiante = randint(1, 100)            # generamos un número de identificación aleatorio
    if estudiante not in estudiantesB:
        estudiantesB.append(estudiante)

estudiantesB.sort()

print(" Materia A: ",estudiantesA,"\n",
      "Materia B: ",estudiantesB)

# Crear una lista con los estudiantes matriculados en ambas materias.
estudiantesComunes = [ ]
for i in estudiantesA:
    if i in estudiantesB:
            estudiantesComunes.append(i)
            estudiantesA.remove(i)                # Eliminamos de la lista A los que estan matriculados en ambas.

print(" Estudiantes matriculados en ambas materias: ",estudiantesComunes,"\n",
      "Total estudiantes matriculados en A y B: ",len(estudiantesComunes),"\n",
      "Estudiantes que solo están matriculados en la materia A: ", len(estudiantesA), estudiantesA)


"""Calcular el perímetro de un polígono."""

# 1. Crear el vector de las abscisas.
# 2. Crear el vector de las ordenadas.
# 3. Calcular la longitud de cada uno de los lados del polígono.
# 4. Sumar la longitud de todos los lados.

print("\n")
# Determinar el número de lados y de vertices del polígono.
while True:
    numeroLados = ValidarEntero("Lados del polígono: ", "Error, ingrese un número entero mayor que dos.")

    if numeroLados < 3:                             # Validamos que el polígono sea mínimo un tríangulo.
        print("Error, ingrese un número entero mayor que dos.")
        continue

    break

# Vectores de abscisas y de ordendas.
abscisas = [ ]
ordenadas = [ ]
for i in range(numeroLados):
    abscisa = ValidarReal("Abscisa: ", "Error, ingrese un número.")
    abscisas.append(abscisa)
    ordenada = ValidarReal("Ordenada: ", "Error, ingrese un número.")
    ordenadas.append(ordenada)

# Almacenar la sumatoria de las longitudes de los lados.
perimetroPoligono = sqrt(pow(abscisas[0] - abscisas[len(abscisas)-1], 2) +
                         pow(ordenadas[0] - ordenadas[len(ordenadas)-1],2))

for j in range(1, len(abscisas)):
    longitudLado = sqrt(pow(abscisas[j] - abscisas[j-1], 2) +
                        pow(ordenadas[j] - ordenadas[j-1],2))

# Lista de vertices del polígono.
vertices = zip(abscisas, ordenadas)
listaVertices = list(vertices)
print(" Vértices: ",listaVertices,"\n",
      "Perímetro: ",format(perimetroPoligono, ".4f"))

