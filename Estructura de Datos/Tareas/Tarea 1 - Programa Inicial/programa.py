archivo = open("datos.csv", "r")

linea = archivo.readline()
linea = archivo.readline()
linea = archivo.readline()
linea = archivo.readline()
linea = archivo.readline()
linea = archivo.readline()
linea = archivo.readline()
linea = archivo.readline()
linea = archivo.readline()

datos = linea.split(",")

enero = int(datos[3])
junio = int(datos[8])

print("Seguidores en enero:", enero)
print("Seguidores en junio:", junio)

diferencia = junio - enero
print("Diferencia de seguidores entre enero y junio:", diferencia)

mes1 = input("Escribe el primer mes: ")
mes2 = input("Escribe el segundo mes: ")

if mes1 == "enero":
    posicion1 = 3
elif mes1 == "febrero":
    posicion1 = 4
elif mes1 == "marzo":
    posicion1 = 5
elif mes1 == "abril":
    posicion1 = 6
elif mes1 == "mayo":
    posicion1 = 7
elif mes1 == "junio":
    posicion1 = 8

print("Posición del mes", mes1, ":", posicion1)

if mes2 == "enero":
    posicion2 = 3
elif mes2 == "febrero":
    posicion2 = 4
elif mes2 == "marzo":
    posicion2 = 5
elif mes2 == "abril":
    posicion2 = 6
elif mes2 == "mayo":
    posicion2 = 7
elif mes2 == "junio":
    posicion2 = 8

print("Posición del mes", mes2, ":", posicion2)


archivo = open("datos.csv", "r")
linea = archivo.readline()

while linea != "":
    if "YOUTUBE,VISUALIZACIONES" in linea:
        yt = linea.split(",")
        visualizacion1 = int(yt[posicion1])
        visualizacion2 = int(yt[posicion2])
        print(linea)
        print("mes 1:", visualizacion1)
        print("mes 2:", visualizacion2)

        diferencia = visualizacion2 - visualizacion1

        print("Diferencia de visualizaciones entre", mes1, "y", mes2, ":", diferencia)
        break

    linea = archivo.readline()


archivo = open("datos.csv", "r")
linea = archivo.readline()

while linea != "":
    if "TWITTER,CRECIMIENTO DE FOLLOWERS" in linea:
        x = linea.split(",")
        seguidores1 = int(x[3])
        seguidores2 = int(x[4])
        seguidores3 = int(x[5])
        seguidores4 = int(x[6])
        seguidores5 = int(x[7])
        seguidores6 = int(x[8])

        print(linea)

        promedio = seguidores1 + seguidores2 + seguidores3 + seguidores4 + seguidores5 + seguidores6

        print("Promedio de seguidores: ", promedio / 6)
        break

    linea = archivo.readline()


archivo = open("datos.csv", "r")
linea = archivo.readline()

while linea != "":
    if "FACEBOOK,CRECIMIENTO" in linea:
        book = linea.split(",")

        follow1 = int(book[3])
        follow2 = int(book[4])
        follow3 = int(book[5])
        follow4 = int(book[6])
        follow5 = int(book[7])
        follow6 = int(book[8])

        print(linea)

        promedio = follow1 + follow2 + follow3 + follow4 + follow5 + follow6

        print("Promedio de seguidores: ", promedio / 6)
        break

    linea = archivo.readline()


archivo = open("datos.csv", "r")
linea = archivo.readline()

while linea != "":
    if "FACEBOOK,ME GUSTA EN PUBLICACIONES" in linea:
        fbook = linea.split(",")

        like1 = int(fbook[3])
        like2 = int(fbook[4])
        like3 = int(fbook[5])
        like4 = int(fbook[6])
        like5 = int(fbook[7])
        like6 = int(fbook[8])

        print(linea)

        promedio = like1 + like2 + like3 + like4 + like5 + like6

        print("Promedio de likes: ", promedio / 6)
        break

    linea = archivo.readline()


archivo = open("datos.csv", "r")
linea = archivo.readline()

while linea != "":
    if "TWITTER,ME GUSTA" in linea:
        xtwit = linea.split(",")

        gusta1 = int(xtwit[3])
        gusta2 = int(xtwit[4])
        gusta3 = int(xtwit[5])
        gusta4 = int(xtwit[6])
        gusta5 = int(xtwit[7])
        gusta6 = int(xtwit[8])

        print(linea)

        promedio = gusta1 + gusta2 + gusta3 + gusta4 + gusta5 + gusta6

        print("Promedio de me gusta: ", promedio / 6)
        break

    linea = archivo.readline()


archivo = open("datos.csv", "r")
linea = archivo.readline()

while linea != "":
    if "YOUTUBE,ME GUSTA" in linea:
        ytlike = linea.split(",")

        megusta1 = int(ytlike[3])
        megusta2 = int(ytlike[4])
        megusta3 = int(ytlike[5])
        megusta4 = int(ytlike[6])
        megusta5 = int(ytlike[7])
        megusta6 = int(ytlike[8])

        print(linea)

        promedio = megusta1 + megusta2 + megusta3 + megusta4 + megusta5 + megusta6

        print("Promedio de me gusta: ", promedio / 6)
        break

    linea = archivo.readline()


archivo.close()