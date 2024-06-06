lista_menor70 = []
lista_mayor70 = []
dia = 1

while True:

    puntaje = int(input("Ingrese puntaje del alumno (1 a 100): "))
    if puntaje < 1 or puntaje > 100:
        print("")
        print("Puntaje ingresado no válido. Ingrese nuevamente")
        print("")

    elif puntaje >= 1 and puntaje < 70:
        parseo = str(dia)
        a = "Día " + parseo
        lista_menor70.append(a)
        dia = dia + 1

        if dia >= 16:
            break

    elif puntaje >= 70 and puntaje <= 100:
        parseo = str(dia)
        a = ("Día " + parseo)
        lista_mayor70.append(a)
        dia = dia + 1

        if dia >= 16:
            break

print("")
print("Los días que recibieron un puntaje menor a 70 puntos son: ")
print(lista_menor70)
print("")
print("Los días que recibieron un puntaje mayor o igual a 70 puntos son: ")
print(lista_mayor70)

