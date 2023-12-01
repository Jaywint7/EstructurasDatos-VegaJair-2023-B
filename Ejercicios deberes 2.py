"""print ("------------------------------------------------")
print ("Ejercicios - Estructura de condición")
print ("Por Jair Vega\n")
## Ejercicio 1   ---- Jair Vega

letra = input("Ingrese una sola letra: ")

if letra.isalpha() and letra.isupper() and len(letra) == 1:
    # .isalpha() verifica si la cadena está formada únicamente por letras 
    # .isupper() verifica si todas las letras son mayúsculas. 
    # len()==1 lee la cadena y que sea igual a 1
    print("La letra ingresada es una letra mayúscula.")
else:
    print("La letra ingresada es una letra minúscula.")
print ("------------------------------------------------")
print ("Ejercicios - Estructura de condición")
print ("Por Jair Vega\n")
## Ejercicio 2   ---- Jair Vega
nota = int(input("Ingrese su nota: "))
edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo (M)-Masculino y F-(Femenino): ")

if nota >= 5 and edad >= 18:
    if sexo == "F":
        print("ACEPTADA")
    elif sexo == "M":
        print("POSIBLE")
    else:
        print("NO ACEPTADA")
else:
    print("NO ACEPTADA")
print ("------------------------------------------------")
print ("Ejercicios - Estructura de condición")
print ("Por Jair Vega\n")
## Ejercicio 3   ---- Jair Vega
print ("Algoritmo que pida tres números y los muestre ordenados (de mayor a menor)\n")
n_1 = int(input("Ingrese el primer número: "))
n_2 = int(input("Ingrese el segundo número: "))
n_3 = int(input("Ingrese el tercer número: "))

if n_1>n_2>n_3:
    print ("El orden es el siguiente: ",n_1,"-",n_2,"-",n_3)
elif n_1>n_3>n_2:
    print ("El orden es el siguiente: ",n_1,"-",n_3,"-",n_2)
elif n_2>n_3>n_1:
    print ("El orden es el siguiente: ",n_2,"-",n_3,"-",n_1)
elif n_2>n_1>n_3:
    print ("El orden es el siguiente: ",n_2,"-",n_1,"-",n_3)
elif n_3>n_1>n_2:
    print ("El orden es el siguiente: ",n_3,"-",n_1,"-",n_2)
elif n_3>n_2>n_1:
    print ("El orden es el siguiente: ",n_3,"-",n_2,"-",n_1)
else:
    print("Ingrese lo que se le solicita")
print ("------------------------------------------------")
print ("Ejercicios - Estructura de condición")
print ("Por Jair Vega\n")

## Ejercicio 4   ---- Jair Vega
print ("Determinar el tipo de triángulo a partir de sus lados\n")
A = float(input("Ingrese la longitud del lado A: "))
B = float(input("Ingrese la longitud del lado B: "))
C = float(input("Ingrese la longitud del lado C: "))

if (A + B) > C and (A + C) > B and (B + C) > A:
    if (A**2 + B**2 == C**2) or (A**2 + C**2 == B**2) or (B**2 + C**2 == A**2):
        print(" -- El Triángulo es Rectángulo -- ")
    elif A == B and B == C:
        print(" -- El Triángulo es Equilátero -- ")
    elif A == B or B == C or A == C:
        print(" -- El Triángulo es Isósceles -- ")
    else:
        print(" -- El Triángulo es Escaleno -- ")
else:
    print("No se logro identificar el Triángulo")
print ("------------------------------------------------")
print ("Ejercicios - Estructura de condición")
print ("Por Jair Vega\n")
## Ejercicio 5   ---- Jair Vega
print ("Determinar la ganancia por la venta de uva\n")
tipo = input("Ingrese el tipo de uva que desea comprar (A o B): ")
tamaño = int(input("Ingrese el atamaño de uva que desea comprar (1 o 2): "))
precio = float(input("Ingrese el precio inicial al kilo de uva en euros: "))
ganancia = 0
if tipo == "A" or tipo == "a":
    if tamaño == 1:
        ganancia = precio + 0.20
    elif tamaño == 2:
        ganancia = precio + 0.30
if tipo == "B" or tipo == "b":
    if tamaño == 1:
        ganancia = precio - 0.30
    elif tamaño == 2:
        ganancia = precio - 0.50
print("\nLa ganancia obtenida por la venta de uvas es de:",ganancia,"euros por kilo")
print ("------------------------------------------------")
print ("Ejercicios - Estructura de condición")
print ("Por Jair Vega\n")
## Ejercicio 6   ---- Jair Vega
print ("Determinar el pago a la compañía de autobuses y a cada alumno\n")
alumnos = int(input("Ingrese el número de alumnos en el viaje de estudios: "))

if alumnos >= 100:
    costo_Alumno = 65
elif 50 <= alumnos <= 99:
    costo_Alumno = 70
elif 30 <= alumnos <= 49:
    costo_Alumno = 95
else:
    costo_Alumno = 0 
    total_Compan = 4000
    print("El costo fijo por el autobús es de 4000 euros")

if costo_Alumno != 0:
    total_Compan = costo_Alumno * alumnos
    print(f"El costo por alumno es de",costo_Alumno,"euros")
    print(f"El total a pagar a la compañía de autobuses es de",total_Compan,"euros")

costo_Talumnos = costo_Alumno * alumnos

print(f"\nCada alumno debe pagar",costo_Alumno,"euros")
print(f"El costo total para los", alumnos,"alumnos es de",costo_Talumnos,"euros")
print ("------------------------------------------------")
print ("Ejercicios - Estructura de condición")
print ("Por Jair Vega\n")
## Ejercicio 7   ---- Jair Vega
print ("El costo por servicio de transportey la zona a la que va dirigido\n")
print("-- Usamos la siguiente conversión:  1kg ----> 1000g --")
peso = float(input("Ingrese el peso del paquete (gramos): "))
if peso>0 and peso<=5000:
    print ("Escoja una la zona quiere repartir:")
    print ("1. América del Norte:")
    print ("2. América Central:")
    print ("3. América del Sur:")
    print ("4. Europa:")
    print ("5. Asia:")
    zona = int(input("Escoja la zona (1-5): "))
    if zona == 1:
        print("El coste es de:",peso*24,"euros")
    elif zona == 2:
        print("El coste es de:",peso*20,"euros")
    elif zona == 3:
        print("El coste es de:",peso*21,"euros")
    elif zona == 4:
        print("El coste es de:",peso*10,"euros")
    elif zona == 5:
        print("El coste es de:",peso*18,"euros")
    else:
        print("Zona no válida.")
else:
    print("Peso incorrecto, ingrese un peso acorde el protocolo (5kg - 5000g)")
print ("------------------------------------------------")
print ("Ejercicios - Estructura de condición")
print ("Por Jair Vega\n")
## Ejercicio 8   ---- Jair Vega
print ("Pedir el día y escriba el día\n")
dia = int(input("Ingrese un número del 1 al 7 para determinar el día: "))
if dia == 1:
    print("El día es Lunes")
elif dia == 2:
    print("El día es Martes")
elif dia == 3:
    print("El día es Miercoles")
elif dia == 4:
    print("El día es Jueves")
elif dia == 5:
    print("El día es Viernes")
elif dia == 6:
    print("El día es Sábado")
elif dia == 7:
    print("El día es Domingo")       
else:
    print("Error - Ingrese solo del 1 al 7")
print ("------------------------------------------------")
print ("Ejercicios - Estructura de condición")
print ("Por Jair Vega\n")
## Ejercicio 9   ---- Jair Vega
def dimeTipoMotor():
    tipo_motor = int(input("Escoja opcion del tipo de motor (1 - 2 - 3 - 4): "))

    switch = {
        0: "No hay establecido un valor definido para el tipo de bomba",
        1: "La bomba es una bomba de agua",
        2: "La bomba es una bomba de gasolina",
        3: "La bomba es una bomba de hormigón",
        4: "La bomba es una bomba de pasta alimenticia",
    }
    #Hace la prueba si se ingresa un número no definido
    mensaje = switch.get(tipo_motor, "No existe un valor válido para tipo de bomba")
    print(mensaje)

dimeTipoMotor()"""
print ("------------------------------------------------")
print ("Ejercicios - Estructura de condición")
print ("Por Jair Vega\n")
## Ejercicio 8   ---- Jair Vega
print ("Notas del Estudiante\n")
nombre = input("Ingrese su nombre y apellido: ")
nota = float(input("Ingrese las nota de Inglés sobre 10: "))

print("-----------------------------------------")
print("Su nota es la siguiente: ",nota)
print("Por tanto:")
print("-----------------------------------------")
if (nota>=9 and nota<=10):
    print("Felicitaciones",nombre,", su nota es",nota,"equivalente a excelente")
elif(nota>=7 and nota<9):
    print("Siga adelante",nombre,", su nota es",nota,"equivalente a muy buena")
elif(nota>=5 and nota<7):
    print("Debe esforzarse más",nombre,", su nota es",nota,"equivalente a buena")
elif(nota>=0 and nota<5):
    print("Usted puede reprobar",nombre,", ya que su nota es",nota,"equivalente a regular")
else:
    print("Nota fuera de rango / No se puede determinar")

