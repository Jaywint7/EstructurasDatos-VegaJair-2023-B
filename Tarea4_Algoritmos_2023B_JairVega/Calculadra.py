print("--------------------------------------------")
print("            CALCULADORA BASICA              ")
print("                 JAIR VEGA                  ")
print("--------------------------------------------")
print("Tenemos las siguientes operaciones")
print("1. Suma")
print("2. Resta ")
print("3. Multiplicación")
print("4. División")
print("5. Potencia")
print("6. Módulo")
print("--------------------------------------------")
opc = int(input("Ingrese el numero de la operación a escoger: "))
print("--------------------------------------------")
match opc:
    case 1:
        n1 = float(input("Ingrese el primer valor: "))
        n2 = float(input("Ingrese el segundo valor: "))
        suma = n1 + n2
        print("--------------------------------------------")
        print("El valor total de ",n1," + ",n2," = ",suma)  
        print("--------------------------------------------")
    case 2:
        n1 = float(input("Ingrese el primer valor: "))
        n2 = float(input("Ingrese el segundo valor: "))
        rest = n1 - n2
        print("--------------------------------------------")
        print("El valor total de ",n1," - ",n2," = ",rest)
        print("--------------------------------------------")  
    case 3:
        n1 = float(input("Ingrese el primer valor: "))
        n2 = float(input("Ingrese el segundo valor: "))
        mult = n1 * n2
        print("--------------------------------------------")
        print("El valor total de ",n1," * ",n2," = ",mult)
        print("--------------------------------------------")
    case 4:
        n1 = float(input("Ingrese el primer valor: "))
        n2 = float(input("Ingrese el segundo valor: "))
        if n2!=0:
            div = n1 / n2
            print("--------------------------------------------")
            print("El valor total de ",n1," / ",n2," = ",div)
            print("--------------------------------------------")
        else:
            print("--------------------------------------------")
            print("ERROR - No existe división para 0")
            print("--------------------------------------------")
    case 5:
        n1 = float(input("Ingrese el valor: "))
        potencia = int(input("Ingrese la potencia a la cual desea elevar: "))
        pot = n1**potencia
        print("--------------------------------------------")
        print("El valor de ",n1,"^",potencia," = ",pot)
        print("--------------------------------------------")
    case 6:
        n1 = float(input("Ingrese el primer valor: "))
        n2 = float(input("Ingrese el segundo valor: "))
        if n2!=0:
            mod = n1 % n2
            print("--------------------------------------------")
            print("El valor total del modulo es ",n1," % ",n2," = ",mod)
            print("--------------------------------------------")
        else:
            print("--------------------------------------------")
            print("ERROR - No existe división para 0")
            print("--------------------------------------------")
    case other: 
        print("--------------------------------------------")       
        print("ERROR - Escoja una opción del menú")
        print("--------------------------------------------")


