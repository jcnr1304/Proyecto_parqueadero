#Juan Niño - Proyecto integrador
import json
#-* coding utf-8 -*-
#registro
def registro(Usuarios_parqueadero):
    nuevo_usuario = []
    #Nombre
    Nombre = input("Digite su nombre completo: ")
    nuevo_usuario.append(Nombre)
    #Mirar si ya existe el ID
    lista_de_Id_existentes = []
    #Añadir Ids a la lista 
    for fila in Usuarios_parqueadero:
        lista_de_Id_existentes.append(fila[1])
    Id = int(input("Digite su número de identificación: "))
    while Id in lista_de_Id_existentes:
        print("Este Id ya existe")
        return Usuarios_parqueadero
    nuevo_usuario.append(Id)
    #Tipo de usuario
    Tipo_de_usuario = input("Digite si eres Estudiante, Profesor o Personal Administrativo: ")
    nuevo_usuario.append(Tipo_de_usuario)
    #Placa
    Placa = input("Digite la placa de tu vehículo: ")
    nuevo_usuario.append(Placa)
    #Tipo de vehículo
    Tipo_de_vehiculo = input("Digite el tipo de vehículo que manejas; Automóvil, Eléctrico, Motocicleta, Discapacitado :")
    nuevo_usuario.append(Tipo_de_vehiculo)
    #Plan de pago
    Plan_de_pago = input("Digite si quiere pagar por Mensualidad o Diaro: ")
    nuevo_usuario.append(Plan_de_pago)
    #añadir nuevo usuario
    Usuarios_parqueadero.append(nuevo_usuario)
    print("Se agregó el nuevo usuario")
    return Usuarios_parqueadero


def entradaV(Vehiculos_parqueadero):
    nuevo_vehiculo = []
    Placa = input("Digite la placa de tu vehículo: ")
    #Añadir  a la lista placas 
    lista_de_Placas_existentes =[]
    for fila in Vehiculos_parqueadero:
        lista_de_Placas_existentes.append(fila[3])
    if Placa in lista_de_Placas_existentes :
        print("Esta vehiculo se encuentra registrada \n")
        nuevo_vehiculo.append(Placa)
        print("Se ha registrado la entrada \n")
    else:
        print("Se debe regitrar este vehiculo")
        registro(Usuarios_parqueadero)

    return Vehiculos_parqueadero
#   sacar un vehiculo del parqueadero 

def salidaV(Vehiculos_parqueadero):
    salida_vehiculo = []
    Placa = input("Digite la placa de tu vehículo: ")
    #Añadir  a la lista placas 
    lista_de_Placas_existentes =[]
    for fila in Vehiculos_parqueadero:
        lista_de_Placas_existentes.append(fila[3])
    if Placa in lista_de_Placas_existentes :
        del Placa
        print("Salida Correcta\n")
    else:
        print("Se debe regitrar este vehiculo")
        registro(Usuarios_parqueadero)

    return Vehiculos_parqueadero
#

#vehículos parqueados según tipo de usuario




def reporte1 (Usuarios_parqueadero):
    #se abre el txt
    filename = str(input("Digite el nombre del archivo donde deseas ver el reporte de vehículos parqueados según el tipo de usuario (agregue .txt al final): "))
    file  =  open (filename,  "w" )
    file.write( "Reporte de cantidad de vehículos según tipo de Usuario: \n" )
    #se crean contadores
    contador_e = 0
    contador_p = 0
    contador_a = 0
    contador_v = 0
    #cuando la lista tenga personas parqueadas, va a revisar la posición 2 y ver el tipo de usuario
    for usuario in Usuarios_parqueadero:
        tipo_de_usuario = usuario[2]
        if tipo_de_usuario == "Estudiante":
            contador_e += 1
        elif tipo_de_usuario == "Profesor":
            contador_p += 1
        elif tipo_de_usuario == "Personal Administrativo":
            contador_a += 1
        elif tipo_de_usuario == "Visitante":
            contador_v += 1
    file.write("La cantidad de Estudiantes parqueados es de: " + str(contador_e) + "\n")
    file.write("La cantidad de Profesores parqueados es de: " + str(contador_p) + "\n")
    file.write("La cantidad de Administrativos parqueados es de: " + str(contador_a) + "\n")
    file.write("La cantidad de Visitantes parqueados es de: " + str(contador_v) + "\n")
    file.close ()
    print("Se generó el archivo \n")

#vehículos parqueados según tipo de vehículo
def reporte2 (Usuarios_parqueadero): 
    #se abre el txt
    filename = str(input("Digite el nombre del archivo donde deseas ver el reporte de vehículos parqueados según el tipo de Vehículo (agregue .txt al final): "))
    file  =  open (filename,  "w" )
    file.write( "Reporte de cantidad de vehículos según tipo de Vehículo: \n" )
    #se crean contadores
    contador_a = 0
    contador_e = 0
    contador_m = 0
    contador_d = 0
    #cuando la lista tenga personas parqueadas, va a revisar la posición 4 y ver el tipo de usuario
    for usuario in Usuarios_parqueadero:
        tipo_de_vehiculo = usuario[4]
        if tipo_de_vehiculo == "Automóvil":
            contador_a += 1
        elif tipo_de_vehiculo == "Eléctrico":
            contador_e += 1
        elif tipo_de_vehiculo == "Motocicleta":
            contador_m += 1
        elif tipo_de_vehiculo == "Discapacitado":
            contador_d += 1
    file.write("La cantidad de Automóviles parqueados es de: " + str(contador_a) + "\n")
    file.write("La cantidad de Automóviles eléctricos parqueados es de: " + str(contador_e) + "\n")
    file.write("La cantidad de Motocicletas parqueados es de: " + str(contador_m) + "\n")
    file.write("La cantidad de Discapacitados parqueados es de: " + str(contador_d) + "\n")
    file.close ()
    print("Se generó el archivo \n")

#porcentaje de ocupación
def reporte3 (Usuarios_parqueadero):
    #se abre el txt
    filename = str(input("Indica el nombre del archivo donde deseas ver el porcentaje de ocupacion del parqueadero (agregue .txt al final): "))
    file  =  open (filename,  "w" )
    file.write( "Reporte de porcentaje de ocupación del parqueadero: \n" )
    #se crean contadores
    porcentaje_total = 0
    porcentaje_Piso1 = 0
    porcentaje_Piso2 = 0
    porcentaje_Piso3 = 0
    porcentaje_Piso4 = 0
    porcentaje_Piso5 = 0
    porcentaje_Piso6 = 0
    #cuando la lista tenga personas parqueadas, va a revisar la posición 6 y ver el tipo de usuario
    for usuario in Usuarios_parqueadero:
        piso_de_parqueo = usuario[6]
        if piso_de_parqueo == "1":
            porcentaje_Piso1 += 1
        elif piso_de_parqueo == "2":
            porcentaje_Piso2 += 1
        elif piso_de_parqueo == "3":
            porcentaje_Piso3 += 1
        elif piso_de_parqueo == "4":
            porcentaje_Piso4 += 1
        elif piso_de_parqueo == "5":
            porcentaje_Piso5 += 1
        elif piso_de_parqueo == "6":
            porcentaje_Piso6 += 1
    porcentaje_Piso6 = porcentaje_Piso6 / 50 * 100
    porcentaje_total = len(Usuarios_parqueadero) / 550 * 100
    file.write("El porcentaje de ocupacion total es de: " + str(porcentaje_total) + "% \n")
    file.write("El porcentaje de ocupacion del Piso 1 es de:" + str(porcentaje_Piso1) + "% \n")
    file.write("El porcentaje de ocupacion del Piso 2 es de:" + str(porcentaje_Piso2) + "% \n")
    file.write("El porcentaje de ocupacion del Piso 3 es de:" + str(porcentaje_Piso3) + "% \n")
    file.write("El porcentaje de ocupacion del Piso 4 es de:" + str(porcentaje_Piso4) + "% \n")
    file.write("El porcentaje de ocupacion del Piso 5 es de:" + str(porcentaje_Piso5) + "% \n")
    file.write("El porcentaje de ocupacion del Piso 6 es de:" + str(porcentaje_Piso6) + "% \n")
    file.close ()
    print("Se generó el archivo \n")


#Mostrar matriz (cualquier piso se muestra con esto)
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)
    print("")

#Usuarios_parqueadero
with open('usuarios.json') as file:
    Usuarios_parqueadero = json.load(file)
#Definir matriz de Usuarios_parqueadero
Usuarios_parqueadero = Usuarios_parqueadero["usuarios"][:]

#Vehiculos_parqueadero
with open('usuarios.json') as file:
    Vehiculos_parqueadero = json.load(file)
#Definir matriz de Vehiculos_parqueadero
Vehiculos_parqueadero = Vehiculos_parqueadero["usuarios"][:]

#Parqueadero
with open('tiposParqueaderos.json') as file:
    parqueadero = json.load(file)

#Pisos
Piso1 = parqueadero["Piso1"][:]
#definir pisos con 0
Piso1_espacios = []
for i in range(10):
    Piso1_espacios.append([])
    for j in range(10):
        Piso1_espacios[i].append(0)

#Pisos
Piso2 = parqueadero["Piso2"][:]
#definir pisos con 0
Piso2_espacios = []
for i in range(10):
    Piso2_espacios.append([])
    for j in range(10):
        Piso2_espacios[i].append(0)

#Pisos
Piso3 = parqueadero["Piso3"][:]
#definir pisos con 0
Piso3_espacios = []
for i in range(10):
    Piso3_espacios.append([])
    for j in range(10):
        Piso3_espacios[i].append(0)

#Pisos
Piso4 = parqueadero["Piso4"][:]
#definir pisos con 0
Piso4_espacios = []
for i in range(10):
    Piso4_espacios.append([])
    for j in range(10):
        Piso4_espacios[i].append(0)

#Pisos
Piso5 = parqueadero["Piso5"][:]
#definir pisos con 0
Piso5_espacios = []
for i in range(10):
    Piso5_espacios.append([])
    for j in range(10):
        Piso5_espacios[i].append(0)

#Pisos
Piso6 = parqueadero["Piso6"][:]
#definir pisos con 0
Piso6_espacios = []
for i in range(10):
    Piso6_espacios.append([])
    for j in range(5):
        Piso6_espacios[i].append(0)
    
#matriz de personas parqueadas (se colocan algunas personas ya registradas solo para probar)
personas_parqueadas = [["Dick Safford", 68433071, "Personal Administrativo", "LML817", "Automóvil", "Diario","1"],
		["Seely Salazar", 60844675, "Personal Administrativo", "CGH793", "Discapacitado", "Diario","2"],
		["Wakanda Schacht", 87399338, "Personal Administrativo", "BHO805", "Discapacitado", "Mensualidad","6"],
		["Beccalynn Nuno", 92881565, "Personal Administrativo", "JGO075", "Motocicleta", "Diario","4"],
		["Abundiantus Scroggs", 54208046, "Personal Administrativo", "HAN014", "Automóvil Eléctrico", "Mensualidad","4"],
		["Arran Zakrzewski", 52220774, "Personal Administrativo", "BND469", "Automóvil", "Mensualidad","1"],
		["Ludlow Cosenza", 55736674, "Profesor", "GDD423", "Motocicleta", "Diario","2"]]

#Menú
while True:
    print("Bienvenido al parqueadero de la Universidad Javeriana")
    print("¿Qué desea hacer?")
    print("1 Registro")
    print("2 Entrada al parqueadero")
    print("3 Salida del parqueadero")
    print("4 Reporte de vehiculos parqueados según el tipo de usuario")
    print("5 Reporte de vehiculos parqueados según el tipo de vehículo")
    print("6 Reporte de porcentaje de ocupacion")
    print("7. Salir \n")
    opcion = input("Digita la opción que deseas ejecutar: ")
    if opcion == "1":
        print("Registro \n")
        Usuarios_parqueadero = registro(Usuarios_parqueadero)
    elif opcion == "2":
        print("Bienvenido al modulo de registro de parqueadero \n")
        Vehiculos_parqueadero = entradaV(Vehiculos_parqueadero)
        

    elif opcion == "3":
        print("Salir del parqueadero \n")
        salidaV(Vehiculos_parqueadero)
    elif opcion == "4":
        reporte1(Usuarios_parqueadero)
    elif opcion == "5":
        reporte2(Usuarios_parqueadero)
    elif opcion == "6":
        reporte3(Usuarios_parqueadero)
    elif opcion == "7":
        print("Hasta luego, que tenga buen dia \n")
        break
    else:
        print("Escoja una opción valida")

