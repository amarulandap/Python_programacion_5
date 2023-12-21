# Definir un conjunto.

conjunto1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}                     # Directa.
conjunto2 = set(('a', 'b', 'c', 'd', 'e'))                  # A partir de una tupla.

lista1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
conjunto3 = set(lista1)
print("Conjunto 3: ",conjunto3)

st = "Universidad de Antioquia."
print("String convertido en conjunto: ",set(st))

conjunto4 = {3, 5, 7, 9}                                    # Intersección solo muestra los elementos comunes.
print("Intersección entre los conjuntos 1 y 4: ",conjunto1 & conjunto4)

conjunto5 = {'f', 'g', 'h', 'i', 'j'}                       # No repite los elementos comunes.
print("Unión entre los conjuntos 2 y 5: ",conjunto2 | conjunto5)

print("Conjunto 1 - conjunto 4: ",conjunto1 - conjunto4)    # Eliminar los elementos comunes en los dos conjuntos.

print("Conjunto 2 convertido en lista: ",list(conjunto2))   # Convertimos un conjunto en una lista.
# La conversión se realiza ya que los conjuntos no son estructuras indexables.

conjunto4.add(2)
print("Conjunto 4 con el elemento 2 agregado: ",conjunto4)

pertenece = 'j' in conjunto5
print(pertenece)


