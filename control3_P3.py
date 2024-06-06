lista = []

while True:
    palabra = input("Ingrese una palabra (Presione Enter para finalizar): ")
    if palabra == "":
        break
    else:
        lista.append(palabra)

palabra_menor = lista[0]

for palabra in lista:
    if len(palabra) < len(palabra_menor):
        palabra_menor = palabra

caracteres = len(palabra_menor)

print("")
print("La cantidad de caracteres de la palabra más pequeña son:", caracteres)
