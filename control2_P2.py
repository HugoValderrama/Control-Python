lista = []
cont = 0

while True:
    nombre = input("Ingrese nombre: ")
    lista.append(nombre)
    cont = cont + 1

    if cont >= 7:
        break

lista_nueva = lista.copy()

lista_nueva = [nombre for nombre in lista_nueva if not nombre.endswith('a') or nombre.endswith('A')]

print("")
print("Los nombres ingresados que no terminan con la letra a son: ")
print(lista_nueva)
