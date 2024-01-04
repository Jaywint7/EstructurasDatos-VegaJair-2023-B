#Imprimir la tabla de multiplicar de  un numero ingresado
"""num = int(input("Ingrese el numero que desea generar la tabla: "))
i=1
while(i<=12):
     prod = num*i
     print(num,"*",i,"=",prod)   
     i=i+1

#Imprimir los numeros pares hasta el 50
i=2
while(i<=50):
    print(i)
    i=i+2

#Lista para imprimir los numeros pares o impares segun escoja el usuario
num=int(input("Ingrese hasta que numero desea imprimir: "))
print("- Que opcion desea imprimir -")
print("1. Pares")
print("2. Impares")
opcion=int(input("Escoja una opcion: "))
match opcion:
    case 1:
        a=2
        while(a<=num):
            print(a)
            a=a+2
    case 2:
        i=1
        while(i<=num):
            print(i)
            i=i+2
    case other:
        print("Ingresa correctamente")

#Lista para imprimir los numeros pares o impares segun escoja el usuario
num=int(input("Ingrese hasta que numero desea imprimir: "))
print("- Que opcion desea imprimir -")
print("1. Pares")
print("2. Impares")
opcion=int(input("Escoja una opcion: "))
match opcion:
    case 1:
        a=2
        while(a<=num):
            print(a)
            a=a+2
    case 2:
        i=1
        while(i<=num):
            print(i)
            i=i+2
    case other:
        print("Ingresa correctamente")"""

"""#Lista para contar numeros pares o impares
num=int(input("Ingrese la cantidad de numeros que desea: "))
contador=0
contadorp=0
contadori=0
i=1
while(i<=num):
    num2=int(input())
    if (num2%2) == 0:
            contadorp = contadorp+1
    else:
            contadori = contadori+1     
    i=i+1
print("El total de pares es: ", contadorp)
print("El total de impares es: ", contadori)

#Lista para contar numeros pares o impares
num=int(input("Ingrese la cantidad de numeros que desea: "))
contador=0
contadorp=0
contadori=0
while(contador<num):
    num2=int(input("Ingrese el numero: "))
    if num2>0:
        if (num2%2) == 0:
            contadorp = contadorp+1
        else:
            contadori = contadori+1  
        contador+=1 
    else:
        print("ERROR") 
     
print("El total de pares es: ", contadorp)
print("El total de impares es: ", contadori)"""
    
"""#Crear un programa que sume los numeros ingresados por el usuario
num=int(input("Ingrese la cantidad de numeros que desea sumar: "))
contador=0
contadors=0
while(contador<num):
        num2=int(input("Ingrese el numero: "))
        if num2!=0:
            contadors+=num2
            contador+=1
            print("- El resultado de la suma de los numeros ingresados es: ", contadors)
        else:
              print("Fin del programa")"""

#Crear un programa que sume los numeros ingresados por el usuario
"""num=1
contadors=0
cont = 0
while num !=0:
    num=int(input("Ingrese el numero: "))
    contadors+=num
    cont+=1
    print("El numero ingresado es: ",num,", La suma es: ",contadors)
    
print("- El resultado de la suma de los numeros ingresados es: ", contadors) 
prom = round(contadors/(cont-1),2)      
print("- El resultado del promedio de los numeros es: ", prom)"""

"""#For <elemn> in <iterable>:
     #<codigo>
    
n = [4, 7, 8 ,9]
for a in n:
    print(a)
#iterador: recorre los elemtos de un iterable hacia adelante; se puede utilizar con el bucle for
#range: funcion con parametros ---> un parametro(maximo) ---> dos parametros (min, max)/max-1 ---> tres parametros(min, max, step)/max-1
for i in range(0,105,5):
    print(i)

print("Ingrese el numero minimo y maximo")
num2=int(input("Ingrese la cantidad min: "))
num3=int(input("Ingrese la cantidad max: "))
mult=int(input("Ingrese la cantidad del multiplo: "))
for i in range(num2,(num3+1),mult):
    print(i)"""

"""#Fibonacci
numero = int(input("Ingrese un número entero positivo: "))
if numero < 0:
    print("No se puede calcular el factorial de un numero negativo")
else:
    p1 = 1
    p2 = 1
    factorial = 1
    print("La serie Fibonacci hasta el ", numero," termino es: ")
    for i in range(1, numero+1):
        print(p1, " ")
        temp = p1+p2
        p1 = p2
        p2 = temp
        factorial *= i"""

#Factorial
numero = int(input("Ingrese un número entero positivo: "))
if numero < 0:
    print("No se puede calcular el factorial de un numero negativo")
else:
    factorial = 1
    for i in range(2, numero+1):
        factorial *= i
    print("La serie factorial del numero ", numero," es: ", factorial)


