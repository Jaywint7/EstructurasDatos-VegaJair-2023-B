##Ejericio 1
##Jair Vega
nombre = input("Ingrese su nombre: ")
entero = int(input("Ingrese un numero entero: "))
decimal = float(input("Ingrese un numero decimal: "))
complejo = complex(input("Ingrese un numero complejo: "))
print("")
print("El nombre ingresado es: ", nombre)
print("El numero ingresado es: ", entero)
print("El numero decimal ingresado es: ", decimal)
print("El numero complejo ingresado es: ", complejo)

##Ejericio 2
##Jair Vega
#Realizar un programa que ingrese 3 notas y calcular el promedio y asignar una opcion
print("Ingrese las notas del estudiante sobre 10")
print("-----------------------------------------")
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
prom = round(((nota1+nota2+nota3)/3),2)    ##round(numero,2) --> Para que se redondeee a 2 decimales
print("-----------------------------------------")
print("Su nota es la siguiente: ",prom)
print("Por tanto:")
print("-----------------------------------------")
if (prom>=9 and prom<=10):
    print("Felicidades usted completo el ciclo y obtuvo una beca")
elif(prom>=7 and prom<9):
    print("Felicidades usted completo el ciclo")
elif(prom<7):
    print("Lo sentimos usted reprobo el ciclo")
else:
    print("Nota fuera de rango / No se puede determinar")

##Ejericio 3
##Jair Vega
print("Ingrese sus Datos")
nombre = input("Ingrese su nombre completo: ")
curso = input("Ingrese la materia a la cual desea inscribirse: ")
aula = int(input("Ingrese el numero del aula: "))
hora = input("Ingrese el horario que desea: ")
print("------------------------------------------")
print("Bienvenido al curso de",curso)
print("Su nombre es el siguiente: ", nombre)
print("El curso inscrito es de: ", curso)
print("El aula escogida es: ", aula)
print("El hora escogido es el siguiente ingresado es: ", hora)

##Ejericio 4
##Jair Vega
import math
ctoMy = float(input("Ingrese un numero: "))
ctoMn = float(input("Ingrese otro numero: "))

hip1 = (math.sqrt(ctoMy**2+ctoMn**2))
hip2 = math.sqrt(pow(ctoMy,2)+pow(ctoMn,2))

print("El resultado de la hipotenusa (Usando el ** para elevar al 2)): ",hip1)
print("El resultado de la hipotenusa (Usando la funcion - pow(potencia))): ",hip2)


##Ejericio 5
##Jair Vega
#Realizar un programa que ingrese 3 notas y calcular el promedio y asignar una opcion
print("Ingrese las notas del estudiante sobre 10")
print("-----------------------------------------")
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
prom = round(((nota1+nota2+nota3)/3),2)    ##round(numero,2) --> Para que se redondeee a 2 decimales
print("-----------------------------------------")
print("Su nota es la siguiente: ",prom)
print("Por tanto:")
print("-----------------------------------------")
if (prom>=9 and prom<=10):
    print("Felicidades usted completo el ciclo y obtuvo una beca")
elif(prom>=7 and prom<9):
    print("Felicidades usted completo el ciclo")
elif(prom<7):
    print("Lo sentimos usted reprobo el ciclo")
else:
    print("Nota fuera de rango / No se puede determinar")

##Ejericio 6
# ##Jair Vega
num = int(input("Ingrese un numero: "))
if(num<=10):
    print("El numero es menor que 10 ---- ", num)

##Ejericio 7
# ##Jair Vega
lista = [1, 2, 3, 4, 7]
tupla = [1, 0, 5, 4, 9]
diccionario = {'a':2, 'b':4, 'c':8}
print(lista)
print(tupla)
print(diccionario)
    
