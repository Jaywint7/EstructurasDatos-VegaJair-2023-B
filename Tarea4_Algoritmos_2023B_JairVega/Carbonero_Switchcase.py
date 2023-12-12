print("--------------------------------------------")
print("EJERCICIO PRUEBA COMPLEMENTARIA - SWITCHCASE")
print("                JAIR VEGA                   ")
print("--------------------------------------------")
print("**********BIENVENIDOS AL CARBONERO**********")
print("--------------------------------------------")
print("Por favor ingrese los datos para la factura: ")
nombre = input("Ingrese su nombre: ")
cdla = int(input("Ingrese su número de cédula: "))
correo = input("Ingrese su correo electronico: ")
print("--------------------------------------------")
print("Le ofrecemos los siguientes tipos de Hamburguesa: ")
print("1. Sencilla")
print("2. Doble ")
print("3. Triple")
print("--------------------------------------------")
cntdd = int(input("Ingrese la cantidad de Hamburguesas que desea comprar: "))
hmbrg = input("Ingrese las/la Hamburguesa que desea: ")
match hmbrg:
    case "sencilla" | "Sencilla":
        total = cntdd * 1.50
        print ("Por su compra debe cancelar: ",total,"$")
        print("--------------------------------------------")
        print ("Seleccione el tipo de pago")
        print("1. Efectivo")
        print("2. Tarjeta de credito ")
        print("--------------------------------------------")
        pago = int(input("Por favor ingrese un número para indicar el tipo de pago: "))
        print("--------------------------------------------")
        match pago:
            case 1:
                print("Su pago es en efectivo, por favor cancele sin recarga: ",total,"$")
                print(nombre,", muchas gracias por su compra. ¡Vuelva Pronto!")
                print("--------------------------------------------")
                print("- La factura se envió al correo: ",correo,"- ")
            case 2:
                tot2 = round(total*0.05,2)
                print("Su pago es con tarjeta de crédito, deberá cancelar el 5% adicional del pago: ",total+tot2,"$")
                print(nombre,", muchas gracias por su compra. ¡Vuelva Pronto!")
                print("--------------------------------------------")
                print("- La factura se envió al correo: ",correo,"- ")
            case other:
                print("Error(opción inexistente) - Escoja una de las opciones presentadas")
    case "doble" | "Doble":
        total = cntdd * 2.50
        print ("Por su compra debe cancelar: ",total,"$")
        print("--------------------------------------------")
        print ("Seleccione el tipo de pago")
        print("1. Efectivo")
        print("2. Tarjeta de credito ")
        print("--------------------------------------------")
        pago = int(input("Por favor ingrese un número para indicar el tipo de pago: "))
        print("--------------------------------------------")
        match pago:
            case 1:
                print("Su pago es en efectivo, por favor cancele sin recarga: ",total,"$")
                print(nombre,", muchas gracias por su compra. ¡Vuelva Pronto!")
                print("--------------------------------------------")
                print("- La factura se envió al correo: ",correo,"- ")
            case 2:
                tot2 = round(total*0.05,2)
                print("Su pago es con tarjeta de crédito, deberá cancelar el 5% adicional del pago: ",total+tot2,"$")
                print(nombre,", muchas gracias por su compra. ¡Vuelva Pronto!")
                print("--------------------------------------------")
                print("- La factura se envió al correo: ",correo,"- ")
            case other:
                print("Error(opción inexistente) - Escoja una de las opciones presentadas")
    case "triple" | "Triple":
        total = cntdd * 3.25
        print ("Por su compra debe cancelar: ",total,"$")
        print("--------------------------------------------")
        print ("Seleccione el tipo de pago")
        print("1. Efectivo")
        print("2. Tarjeta de credito ")
        print("--------------------------------------------")
        pago = int(input("Por favor ingrese un número para indicar el tipo de pago: "))
        print("--------------------------------------------")
        match pago:
            case 1:
                print("Su pago es en efectivo, por favor cancele sin recarga: ",total,"$")
                print(nombre,", muchas gracias por su compra. ¡Vuelva Pronto!")
                print("--------------------------------------------")
                print("- La factura se envió al correo: ",correo,"- ")
            case 2:
                tot2 = round(total*0.05,2)
                print("Su pago es con tarjeta de crédito, deberá cancelar el 5% adicional del pago: ",total+tot2,"$")
                print(nombre,", muchas gracias por su compra. ¡Vuelva Pronto!")
                print("--------------------------------------------")
                print("- La factura se envió al correo: ",correo,"- ")
            case other:
                print("Error(opción inexistente) - Escoja una de las opciones presentadas")      
    case other: print("Lo sentimos en el Carbonero no ofrecemos este tipo de Hamburguesas")



