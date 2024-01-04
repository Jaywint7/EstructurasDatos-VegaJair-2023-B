print("Ejercicio 1")
print("Jair Vega")
print("-- Calculo de la suma de N pares ---")
numero = int(input('Ingresa el número: '))
sumatoria=0

while int(numero) <= 0 :
  print("Número no válido")
  numero = int(input('Ingresa el número: '))

for i in range(numero+1):
    if(i%2==0):
      sumatoria +=i
      print(i, "+")
    
print("La sumatoria es :", sumatoria)


print("Ejercicio 2")
print("Jair Vega")
print("----- SENSOR DE FUGA -----")
print("Menú de opciones")
print("1.- Verificar el estado de los talleres")
print("2.- Salir")
opcion = int(input("Ingrese la opción: "))

while opcion != 1 and opcion != 2:
  print("Error, verifique las opciones")
  print("1.- Verificar el estado de los talleres")
  print("2.- Salir")
  opcion = int(input("Ingrese la opción: "))
while (opcion != 2):
  print("Ejecutar caso 1")
  contfug = 0
  numtall = 1
  while numtall <= 3:
    print("Existe fuga en el taller ", numtall)
    estado = input("Ingrese si o no: ")
    if estado == "si":
      contfug += 1
    numtall += 1
  if contfug >= 1:
    print("Enviar correo")

  print("1.- Verificar el estado de los talleres")
  print("2.- Salir")
  opcion = int(input("Ingrese la opción: "))

  while opcion != 1 and opcion != 2:
    print("Error, verifique las opciones")
    print("1. Verificar el estado de los talleres")
    print("2. Salir")
    opcion = int(input("Ingrese la opcion: "))

print("Gracias por usar nuestro sistema")


print("Ejercicio 3")
print("Jair Vega")
print("----- Rango -----")
ini = int(input("Ingrese el punto inicial: "))
fin = int(input("Ingrese el punto final: "))
suma = 0
while ini<0 or fin<0:
    print("-----------ERROR-----------")
    print("Deben ser valores positivos")
    ini = int(input("Ingrese el punto inicial: "))
    fin = int(input("Ingrese el punto final: "))

while ini > fin:
    print("-----------ERROR-----------")
    print("El punto inicial debe ser menor que el final")
    ini = int(input("Ingrese el punto inicial: "))
    fin = int(input("Ingrese el punto final: "))

    while ini<0 or fin<0:
      print("-----------ERROR-----------")
      print("Deben ser valores positivos")
      ini = int(input("Ingrese el punto inicial: "))
      fin = int(input("Ingrese el punto final: "))

while ini <= fin:
    suma += ini
print("La sumatoria es: ", suma)

print("Ejercicio 4")
print("Jair Vega")
print("----- Programa Fé y Alegria -----")
print("------ Sistema de calificaciones ------------")

n_calificaciones = 4
sumaCali = 0.0

for i in range(1,5):
  print("Ingresa la calificación ",i,": ",end="")
  calificaciones = float(input())
  sumaCali += calificaciones

print("La suma de calificaciones es: ",sumaCali)
promedio = sumaCali/n_calificaciones
print("El promedio de las calificaciones es: ",promedio)

if promedio >=14:
  print("Aprobado")
elif (9 <= promedio <= 13):
  print("Supletorio")
elif promedio <= 8:
  print("Rechazado")

print("Ejercicio 5")
print("Jair Vega")
print("------- Verificacion Numero ------")
numero = int(input("Ingrese un numero entero positivo: "))
while numero<0 or numero ==0 :
  print("El numero debe ser positivo")
  numero = int(input("Ingrese un numero entero positivo: "))

if 10<=numero<=100:
  print("El número si pertenece al rango")
else:
  print("El número no pertenece al rango")

print("Ejercicio 6")
print("Jair Vega")
print("------- Banco Pichincha --------")

nombre=input("Ingrese el nombre: ")
print("Ingrese el tipo de tarjeta")
tipoTarjeta = int(input("1) o 2) o 3) o 4): "))

while (tipoTarjeta!=1 and tipoTarjeta!=2 and tipoTarjeta!=3 and tipoTarjeta!=4):
  print("Tipo de tarjeta no válido")
  print("Ingrese el tipo de tarjeta")
  tipoTarjeta = int(input("1) o 2) o 3) o 4): "))

creditoAnterior= float((input("Ingrese el crédito actual: ")))
creditoActual = 0.0

def creditoBanco (tipoTrajeta):
  if tipoTarjeta == 1:
    creditoActual = creditoAnterior + (creditoAnterior * 0.25)
    print("El nuevo crédito para su tarjeta es de: ",creditoActual)
  elif tipoTarjeta == 2:
    creditoActual = creditoAnterior + (creditoAnterior * 0.35)
    print("El nuevo crédito para su tarjeta es de: ",creditoActual)
  elif tipoTarjeta == 3:
    creditoActual = creditoAnterior + (creditoAnterior * 0.40)
    print("El nuevo crédito para su tarjeta es de: ",creditoActual)
  else:
    creditoActual = creditoAnterior + (creditoAnterior * 0.50)
    print("El nuevo crédito para su tarjeta es de: ",creditoActual)

creditoBanco(tipoTarjeta)

print("Ejercicio 7")
print("Jair Vega")
print("--------- Etafashion ----------")
prendas = int(input("Ingrese el numero de prendas: "))
while prendas<=0:
  print("Ingrese un numero valido")
  prendas = int(input("Ingrese el numero de prendas: "))

total = float(input("Ingrese el total de la compra: "))
valorFinal=0

if prendas>20:
  valorFinal = total + (total*0.10)
  print("El valor a pagar es de: ",valorFinal)
elif 10<=prendas<=20:
  valorFinal = total + (total*0.05)
  print("El valor a pagar es de: ",valorFinal)
elif prendas<=9:
  print("El valor a pagar es de: ",total)

print("Ejercicio 8")
print("Jair Vega")
print("--------- LA UNIÓN  ---------")

num = int(input("Ingrese el número de guaguas de pan: "))
sumGuaguas = 0
suma = 0
contGuaguas = 0

while contGuaguas <num :
  precioGuagua = float(input(f'Ingrese el precio de la guagua de pan {contGuaguas+1}: '))
  sumGuaguas += precioGuagua
  print("La guagua de pan es de mora?")
  tipoGuagua = input("si o no: ")
  if tipoGuagua == "si":
    suma += 1   
  contGuaguas += 1 
print("----------- Factura-----------------")
print("El total de guaguas de pan a facturar son de ",num)
print("El pecio final a pagar es del $",sumGuaguas)
print("El número de guaguas de mora son de",suma)


print("Ejercicio 9")
print("Jair Vega")
print("------- Sueldazos de la EPN  ---------")

num = int(input("Ingrese el número de empleados a registrar: "))
sumaSueldos = 0
sumaHoras = 0
sumDocentes = 0

for i in range(1,num+1):
  sueldo= float(input(f'Ingrese el sueldo del empleado N°{i}: '))
  sumaSueldos += sueldo
  horas= int(input(f'Ingrese el número de horas que ha trabajado el empleado N°{i}: '))
  sumaHoras += horas
  print("El empleado es docente?")
  docente = input("si o no: ")
  if docente == "si":
    sumDocentes +=1

print("La cantidad de empleados que se han registrado son: ",num)
print("El sueldo de todos los empleados es de",sumaSueldos)
print("El total de horas trabajadas de los empleados es de",sumaHoras)
print("La cantidad de empleados que son docentes son: ",sumDocentes)


print("Ejercicio 10")
print("Jair Vega")
print("------ Menu de opciones ----------")
while True:
    print("Menu de Actividades:")
    print("1. Actividad 1")
    print("2. Actividad 2")

    try:
        opcion = int(input("Ingrese el numero de la actividad o 0 para salir: "))

        if opcion == 0:
            print("Saliendo...")
            break
        elif opcion >= 1 and opcion <= 9:
            print(f"Sintonizando en el Smart TV: Actividad {opcion}")
        else:
            print("ERROR - Ingrese un numero valido o 0 para salir")
    except ValueError:
        print("Ingrese un numero valido")


print("Ejercicio 11")
print("Jair Vega")

total_ahorrado = 0

while True:
    print(" ---- EL JUAN y Produbanco ---")
    print(" ------ Menu de Opciones -------")
    print("1. Ingresar cantidad de dinero del mes")
    print("2. Consultar total ahorrado en el año")
    print("0. Salir")

    try:
        opcion = int(input("Ingrese el numero de la opcion: "))

        if opcion == 0:
            print("Saliendo...")
            break
        elif opcion == 1:
            cantidad_mes = float(input("Ingrese la cantidad de dinero del mes: "))
            total_ahorrado += cantidad_mes
            print(f"Se ha ingresado {cantidad_mes} al ahorro del mes.")
        elif opcion == 2:
            print(f"Total ahorrado en el año: {total_ahorrado}")
        else:
            print("Ingrese una opción valida del menu.")
    except ValueError:
        print("Ingrese un nmero valido.")

