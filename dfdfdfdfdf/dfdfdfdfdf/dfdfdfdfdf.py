
#declara una lista de cadenas

aves=["loro gris", "paloma de diamante", "coctel"]
print("Los valores de la lista antes de insertar: ")
#itera sobre la lista para imprmir los valores

for ave in aves:

    print(ave, end=" ")


print("\n")

#Agrega 3 valores al final de la lista utilizando el metodo append()

aves.append("mayna")
aves.append("periquito")
aves.append("cacatua")
print("Los valores de la lista despues de la tabla: ")
#itera sobre la llista para imprimir los valores

for ave in aves:
    print(ave, end=" ")

    print("\n")
