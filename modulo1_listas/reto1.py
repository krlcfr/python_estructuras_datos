inventario = [
    ["Casco", 5, 150],
    ["Guantes", 10, 50],
    ["Chaqueta", 3, 200]
]

def actualizar_precio():
    nombre = input("Nombre del producto a modificar: ")
    for producto in inventario:
        if producto[0].lower() == nombre.lower():
            nuevo_precio = float(input(f"Nuevo precio para {producto[0]}: "))
            producto[2] = nuevo_precio
            print(f"El precio de {producto[0]} ahora es ${nuevo_precio}.")
            return
    print("No encontramos ese producto, bro.")

def registrar_venta():
    nombre = input("¿Que producto se vendio?: ")
    for producto in inventario:
        if producto[0].lower() == nombre.lower():
            cantidad = int(input(f"¿Cuantas unidades de {producto[0]}?: "))
            if producto[1] >= cantidad:
                producto[1] -= cantidad
                print(f"Venta exitosa. Quedan {producto[1]} unidades de {producto[0]}.")
            else:
                print("No hay suficiente stock. Toca reponer.")
            return
    print("Ese producto no existe en el inventario.")

def añadir_producto():
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad a ingresar: "))
    precio = float(input("Precio del producto: "))
    
    for producto in inventario:
        if producto[0].lower() == nombre.lower():
            producto[1] += cantidad
            print(f"Stock de {producto[0]} actualizado. Ahora hay {producto[1]}.")
            return
            
    inventario.append([nombre, cantidad, precio])
    print(f"Nuevo producto '{nombre}' añadido.")

def mostrar_inventario():
    print("           ESTADO DEL INVENTARIO         ")
    if not inventario:
        print("El inventario esta vacio.")
    else:
        for producto in inventario:
            print(f"Producto: {producto[0]:<12} | Stock: {producto[1]:<4} | Precio: ${producto[2]:.2f}")


def menu():
    while True:
        print("\nSISTEMA DE GESTION DE INVENTARIO")
        print("1. Mostrar inventario")
        print("2. Registrar venta")
        print("3. Añadir o actualizar producto")
        print("4. Actualizar precio")
        print("5. Salir")
        
        opcion = input("Selecciona una opcio: ")
        
        if opcion == "1":
            mostrar_inventario()
        elif opcion == "2":
            registrar_venta()
        elif opcion == "3":
            añadir_producto()
        elif opcion == "4":
            actualizar_precio()
        elif opcion == "5":
            print("Cerrando..bro!")
            break
        else:
            print("Opcion no valida")

menu()