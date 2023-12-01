## Ejercicio 1   ---- Jair Vega
import math
print("El perímetro y área de un rectángulo dada su base y su altura.\n")
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))
perimetro = 2*(base+altura) 
area = altura*base
print("El perímetro del rectángulo es: ", perimetro)
print("El área del rectángulo es: ", area)
print ("------------------------------------------------")
print("El perímetro y área de un círculo dada su radio.\n")
radio = float(input("Ingrese el radio del círculo: "))
pi = 3.141593
perimetro = pi*pow(radio,2)
area = 2*pi*radio
print("El perímetro del rectángulo es: ", perimetro)
print("El área del rectángulo es: ", area)
print ("------------------------------------------------")
print ("Ejercicios - Estructura de secuencia")
print ("Por Jair Vega\n")
## Ejercicio 2   ---- Jair Vega
print("Transformar de Grados Farenheit a Grados Celcius.\n")
far = float(input("Ingrese el dato en Grados Farenheit: "))
conversion = (far-32)*(5/9)
print("--- La conversión de ",far, "°F a Celcius es: ", conversion, "---")
print ("------------------------------------------------")
print ("Ejercicios - Estructura de secuencia")
print ("Por Jair Vega\n")
## Ejercicio 3   ---- Jair Vega
print("Cantidad en minutos y obtener horas y minutos.\n")
min = int(input("Ingrese la cantidad en minutos: "))
horas = int(min/60)
minutos = min % 60
print(min,"minutos son,",horas, "horas y", minutos,"minutos")
print ("------------------------------------------------")
print ("Ejercicios - Estructura de secuencia")
print ("Por Jair Vega\n")
## Ejercicio 4   ---- Jair Vega
print("Vendedor recibe su sueldo aumentado las comisiones.\n")
sueldo = float(input("Ingrese su sueldo: "))
print("--- Aumento de comisión del 10% por venta ---")
print("--- Realizo 3 ventas en el mes = 30% ---")
com = sueldo * 0.3
total = sueldo + com
print("El sueldo total a recibir + comisiones es de: ",total,"$")
print ("------------------------------------------------")
print ("Ejercicios - Estructura de secuencia")
print ("Por Jair Vega\n")
## Ejercicio 5   ---- Jair Vega
print("Alumno desea saber su calificacion final de Algortimos.\n")
print("-- Ingrese sus 3 calificaciones parciales sobre 10 --")
calf_1 = int(input("----- Ingrese primer calificación: "))
calf_2 = int(input("----- Ingrese segunda calificación: "))
calf_3 = int(input("----- Ingrese tercera calificación: ")) 
print("-- Ingrese su calificación del examen final sobre 10 --")
ex_Fnl = int(input("----- Ingrese la calificación del examen: "))
print("-- Ingrese su calificación del trabajo final sobre 10--")
trb_Fnl = int(input("----- Ingrese la calificación del trabajo: "))
prom = (calf_1+calf_2+calf_3)/3
total = (prom*0.55)+(ex_Fnl*0.3)+(trb_Fnl*0.15)
print("\nSu nota final obtenida en la materia de Algoritmos es: ",total)
print ("------------------------------------------------")
print ("Ejercicios - Estructura de secuencia")
print ("Por Jair Vega\n")
## Ejercicio 6   ---- Jair Vega
print("Calcular y mostrar la distancia entre dos pares de puntos en el plano.\n")
print("-- Ingrese los puntos en el plano --")
print("-- Ingrese el primer par de puntos --")
x1 = int(input("Ingrese coordenada en x: "))
y1 = int(input("Ingrese coordenada en y: "))
print("-- Ingrese el segundo par de puntos --")
x2 = int(input("Ingrese coordenada en x: "))
y2 = int(input("Ingrese coordenada en y: "))
print("\nEl primer par es: ","(",x1,";",y1,")")
print("El segundo par es: ","(",x2,";",y2,")")
calculo = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
print("\nLa distancia entre los pares de puntos es de: ",calculo)
print ("------------------------------------------------")
print ("Ejercicios - Estructura de secuencia")
print ("Por Jair Vega\n")
## Ejercicio 7   ---- Jair Vega
print("Calcular y mostrar la distancia entre dos pares de puntos en el plano.\n")
print("-- Ingrese los puntos en el plano --")
print("-- Ingrese el primer par de puntos --")
x1 = int(input("Ingrese coordenada en x: "))
y1 = int(input("Ingrese coordenada en y: "))
print("-- Ingrese el segundo par de puntos --")
x2 = int(input("Ingrese coordenada en x: "))
y2 = int(input("Ingrese coordenada en y: "))
print("\nEl primer par es: ","(",x1,";",y1,")")
print("El segundo par es: ","(",x2,";",y2,")")
calculo = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
print("\nLa distancia entre los pares de puntos es de: ",calculo)
print ("------------------------------------------------")
print ("Ejercicios - Estructura de secuencia")
print ("Por Jair Vega\n")
## Ejercicio 7   ---- Jair Vega
print("Ingrese un número de 2 cifras y despliegue el inverso por pantalla.\n")
num = int(input("Ingrese el número de 2 cifras: "))
cifra1 = int(num/10)
cifra2 = int(num%10)
num_Inv = cifra2*10+cifra1
print("\nEl número invertido es el siguiente: ",num_Inv)
print ("------------------------------------------------")
print ("Ejercicios - Estructura de secuencia")
print ("Por Jair Vega\n")
## Ejercicio 8   ---- Jair Vega
print("Ingrese la distancia entre 2 vehiculos y determine el cruze.")
dist = float(input("Ingrese la distancia entre los vehiculos en km: "))
vel_1 = float(input("Ingrese la velocidad del primer vehículo en km/h: "))
vel_2 = float(input("Ingrese la velocidad del segundo vehículo en km/h: "))

tiempo = dist/(vel_1 - vel_2)
tiempo_Min = tiempo * 60

print("\nEl vehículo más rápido alcanzará al otro en: ",tiempo, "minutos")
print ("------------------------------------------------")
print ("Ejercicios - Estructura de secuencia")
print ("Por Jair Vega\n")
## Ejercicio 9   ---- Jair Vega
print("Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.")
nombre = input("Ingrese su nombre: ")
apell_1 = input("Ingrese su primer apellido: ")
apell_2 = input("Ingrese su segundo apellido: ")

inicial_N = nombre[0]
inicial_A1 = apell_1[0]
inicial_A2 = apell_2[0]

print("\nLas iniciales son: ", inicial_N,".",inicial_A1,".",inicial_A2)
print ("------------------------------------------------")
print ("Ejercicios - Estructura de secuencia")
print ("Por Jair Vega\n")
## Ejercicio 10   ---- Jair Vega
print("Conocer cuanto dinero tiene a partir de monedas de euros.")
mond_2eu = int(input("Ingrese la cantidad de monedas de 2 euros: "))
mond_1eu = int(input("Ingrese la cantidad de monedas de 1 euro: "))
mond_50cent = int(input("Ingrese la cantidad de monedas de 50 céntimos: "))
mond_20cent = int(input("Ingrese la cantidad de monedas de 20 céntimos: "))

total_euros = (mond_2eu * 2) + (mond_1eu * 1) + (mond_50cent * 0.5) + (mond_20cent * 0.2)
total_centavos = int((total_euros % 1) * 100)  #Conv de decimal a céntimo


print("\nTienes un total de: ", int(total_euros),"euros y",total_centavos,"céntimos")