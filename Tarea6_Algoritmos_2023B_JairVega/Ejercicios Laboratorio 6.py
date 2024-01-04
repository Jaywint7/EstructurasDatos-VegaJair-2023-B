"""total = 1000
inicio = 0
print("Ejercicio N1")
print("Jair Vega")
print("-----BANCO 'ANFIELD DESTROY'-----")
cantidad=float(input("Ingrese la cantidad inicial que desea ahorrar: "))
inicio += cantidad

while inicio<total:
    ahorrar=float(input("Ingrese la cantidad de dinero que desea ahorrar: "))
    while ahorrar<0:
        print("ERROR - La cantidad ingresada debe ser positiva")
        ahorrar=float(input("Ingrese la cantidad de dinero que desea ahorrar: "))
    inicio += ahorrar

print("Se ha alcanzado lo maximo de ahorro con un total de ",total,"$")

print("Ejercicio N2")
print("Jair Vega")
print("-----Contar Numeros-----")
numero=int(input("Ingrese un número: "))
numero_str = str(numero) #conversion del numero entero(int) a cadena(string)

contar = len(numero_str) #len la utilizamos para contar la cantidad
                                   #de digitos en la cadena

print("El número de dígitos en ",numero," es: ",contar)

print("Ejercicio N3")
print("Jair Vega")
print("-----Menu repetitivo-----")
while True:
    print("---------------------------")
    print("Menu:")
    print("1. Comenzar programa")
    print("2. Imprimir listado")
    print("3. Finalizar programa")
    print("---------------------------")
    opcion=int(input("Seleccione una opcion del menu prensentado: "))
    print("---------------------------")
    match opcion:
        case 1:
            print("Comenzando programa...")
        case 2:
            print("Imprimiendo listado...")
        case 3:
            print("Finalizando programa. ¡Hasta luego!")
            break
        case other:
            print("Opción incorrecta. Seleccione una opcion del menu")

print("Ejercicio N4")
print("Jair Vega")
print("-----Montos de Compras-----")    
totalcpr = 0

while True:
    monto=float(input("Ingrese el monto de la compra o Ingrese 0 para finalizar: "))

    if monto==0:
        break

    while monto<0:
        print("Error - No hay montos negativos")
        monto=float(input("Ingrese un nuevo monto: "))

    totalcpr += monto

if totalcpr>1000:
    descuento = totalcpr * 0.10
    total = totalcpr - descuento
    print("Total a pagar con 10% de descuento: ",total,"$")
else:
    print("Total a pagar: ",totalcpr,"$")

print("Ejercicio N5")
print("Jair Vega")
print("-----Sistema de Compras-----")    
precios = {
    'Perfumeria': {'Tentacion': 30, 'Primavera': 28, 'Otoño': 15, 'Seduccion': 35},
    'Joyeria': {'Aretes': 7, 'Collar': 5, 'Cadena': 20, 'Pulsera': 15},
    'Ropa': {'Blusa': 25, 'Chaqueta': 60, 'Pantalón': 18, 'Abrigo': 90},
    'Maquillaje': {'Sombras': 8, 'Maquillaje': 5, 'Labiales': 4, 'Rimel': 6}
}
total = 0
# Bucle principal
while True:
    print("--------------------------")
    print(" --- Menu Categorias ---")
    print("1. Perfumeria")
    print("2. Joyeria")
    print("3. Ropa")
    print("4. Maquillaje")
    print("5. Finalizar compra")
    print("--------------------------")
    eleccion = input("Seleccione una categoria (1-5): ")
    print("--------------------------")
    if eleccion == '5':
        print("Compra Finalizada")
        break 

    if eleccion not in {'1', '2', '3', '4'}:
        print("ERROR - Seleccione una categoria valida.")
        continue

    categoria = {
        '1': 'Perfumeria',
        '2': 'Joyeria',
        '3': 'Ropa',
        '4': 'Maquillaje'
    }[eleccion]

    print("Articulos disponibles en: ", categoria)
    for articulo, precio in precios[categoria].items():
        print(articulo," ", precio,"$")
    
    subtotal_categoria = 0

    while True:
        eleccion_articulo = input(f"Seleccione un artículo de {categoria} (o '0' para salir): ")

        if eleccion_articulo == '0':
            print ("Usted salio del menu del articulo")
            break

        if eleccion_articulo not in precios[categoria]:
            print("ERROR - Seleccione un articulo valido.")
            continue

        precio_articulo = precios[categoria][eleccion_articulo]

        while True:
            cantidad_articulo = int(input(f"Ingrese la cantidad de {eleccion_articulo} que desea comprar: "))
            if cantidad_articulo >= 0:
                break
            else:
                print("ERROR - Cantidad no valida")

        subtotal_categoria += precio_articulo * cantidad_articulo
        print(f"Subtotal parcial de {eleccion_articulo}: ${subtotal_categoria}")

        continuar_comprando = input("¿Desea comprar otro articulo de esta categoria? (s/n): ")
        if continuar_comprando.lower() != 's':
            break

    total += subtotal_categoria

print(f"\nResumen de la compra:")
for categoria, items in precios.items():
    cantidad_categoria = sum([int(input(f"Ingrese la cantidad de {item} que desea comprar: ")) for item in items])
    print(f"Cantidad de artículos de {categoria}: {cantidad_categoria}")

print(f"\nTotal de la compra: ${total}")"""


print("Ejercicio N5¿6")
print("Jair Vega")
print("-----Leer cantidades de cadenas-----")  

lineas_completas = 0

while True:
    titulo = input("Libro: ")

    if titulo == "*":
        break

    digitos_numericos = sum(c.isdigit() for c in titulo)

    if titulo == "/":
        print("Linea completa. Aparecen", digitos_numericos, "digitos numericos")
        lineas_completas += 1
    else:
        print("Aparecen ", digitos_numericos, " digitos numericos en ",titulo)

# Mostrar el resultado final
print("- Se leyeron ",lineas_completas, "lineas completas")