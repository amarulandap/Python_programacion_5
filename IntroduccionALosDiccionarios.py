# Crear diccionarios

diccio1 = {1:'Andres', 2:'Ana', 3:'Carlos', 4:'Luisa'}
mujeres = {123:['Anita', 25], 456:['Carmen', 32], 789:['Julia', 28]}

# Accedemos a un elemento del diccionario a través de su clave.
print("Elemento 1 del diccionario 1: ",diccio1[1], "\n"
      "Edad de Carmen: ",mujeres[456][1])

# Modificar un elemento del diccionario.
diccio1[2] = 'Carolina'
mujeres[789][0] = 'Juliana'

# Agregar un nuevo elemento al diccionario.
diccio1[5] = 'Ana'
mujeres[234] = ['Mariana', 26]
print("Diccionario 1: ",diccio1,"\n"
      "Mujeres: ",mujeres)

# Eliminar un elemento de un diccionario.
del diccio1[3]
print("Diccionario 1: ",diccio1)

# Obtener una lista de las claves del diccionario.
clavesMujeres = list(mujeres.keys())
print("Claves de la lista mujeres: ",clavesMujeres)

# Para saber si un elemento esta incluido en la lista, buscamos su clave.
pertenece = 6 in diccio1
print(pertenece)

# Recorrer los elementos de un diccionario.
for i in mujeres:
    # print(i, mujeres[i], end=" ")
    print(i, mujeres[i])




