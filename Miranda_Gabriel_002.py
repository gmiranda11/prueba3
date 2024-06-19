import csv
lista=[]
def validacion(puntos):
    if puntos>=0 and puntos<=150:
        return True
    else:
        return False
def categoria(puntos):
    if puntos>=0 and puntos<=40:
        return "amateur"
    if puntos>=41 and puntos<=80:
        return "principiante"
    if puntos>=81 and puntos<=120:
        return "avanzado"
    if puntos>=120:
        return "idolos"
def confirmacion(resp):
    resp=input("Desea actualizar nombre del equipo? (si/no): ".lower())
    if resp=="si":
        return True
    else:
        return False
def estadisticas(listita):
    acum=0
    prom=0
    mayor=0
    for i in listita:
        acum=acum+int(i[2])
        if int(i[2])>mayor:
            mayor=int(i[2])
    prom=acum/len(listita)
    print("Puntaje promedio: ",prom)
    print("Puntaje mayor: ",mayor)
while True:
    print("")
    print("MENU")
    print("")
    print("1.-Agregar equipo")
    print("2.-Listar equipo")
    print("3.-Actualizar nombre de equipo por id")
    print("4.-Generar BBDD")
    print("5.-Cargar BBDD")
    print("6.-Estadisticas")
    print("0.-Salir")
    print("")
    op=int(input("Ingrese opcion: "))
    if op==1:
        print("")
        print("AGREGAR EQUIPO")
        print("")
        id=int(input("Ingrese ID del equipo: "))
        nombre=input("Ingrese el nombre del equipo: ")
        while True:
            puntos=int(input("Ingrese la cantidad de puntos (0-150): "))
            r=validacion(puntos)
            if r:
                print("Equipo agregado")
                break
            else:
                print("Error, puntos debe ser entre 0 a 150")
        cat=categoria(puntos)
        equipo=[id,nombre,puntos,cat]
        lista.append(equipo)
            
    elif op==2:
        print("")
        print("LISTAR EQUIPOS")
        print("")
        for i in lista:
            print(f"ID: {i[0]} Nombre: {i[1]} Puntos: {i[2]} Categoria: {i[3]}")
    elif op==3:
        encontrado=False
        print("")
        print("ACTUALIZAR NOMBRE DE EQUIPO POR ID")
        print("")
        actualizar=int(input("Ingrese el ID del equipo a actualizar: "))
        for i in lista:
            if int(i[0])==actualizar:
                encontrado=True
                print("Datos de equipo a actualizar: ")
                print(f"ID: {i[0]} Nombre: {i[1]} Puntos: {i[2]} Categoria: {i[3]}")
                r=confirmacion(actualizar)
                if r:
                    #lista.remove(i)
                    nuevonombre=input("Ingrese el nuevo nombre del equipo: ")
                    #me rindo, no me acuerdo como reemplazar
                    break
        if encontrado==False:
            print("ID no encontrado")
    elif op==4:
        print("")
        print("GENERANDO BBDD")
        print("")
        with open ('bbdd.csv','w',newline='') as bbdd:
            escritor_csv = csv.writer(bbdd)
            escritor_csv.writerow(['ID','Nombre','Puntos','Clasificacion'])
            escritor_csv.writerows(lista)
        print("Base de datos generada correctamente")
    elif op==5:
        print("")
        print("CARGANDO BBDD")
        print("")
        lista.clear()
        cont=0
        with open ('bbdd.csv','r',newline='') as bbdd:
            lector_csv = csv.reader(bbdd)
            for i in lector_csv:
                if cont==0:
                    cont=cont+1
                    continue
                id=int(i[0])
                nombre=i[1]
                puntos=int(i[2])
                clasificacion=i[3]
                listab=[id,nombre,puntos,clasificacion]
                lista.append(listab)
        print("Base de datos cargada correctamente")
    elif op==6:
        print("")
        print("ESTADISTICAS")
        print("")
        estadisticas(lista)
    elif op==0:
        print("Adios.")
        break
    else:
        print("Error, ingrese opcion valida")
