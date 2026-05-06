ventas = [
    {"producto": "laptop", "unidades": 20, "precio": 800},
    {"producto": "teclado", "unidades": 50, "precio": 25},
    {"producto": "mouse", "unidades": 30, "precio": 15},
    {"producto": "monitor", "unidades": 10, "precio": 200}
]

def mostrar_valor_total():
    print("\nVALOR TOTAL POR PRODUCTO:")
    valores = [i["unidades"] * i["precio"] for i in ventas]
    for prod, val in zip(ventas, valores):
        print(f"{prod['producto']}: {val}")

def mostrar_productos_mayor_1000():
    print("\nPRODUCTOS CON VALOR > 1000:")
    nombres = [i["producto"] for i in ventas if i["unidades"] * i["precio"] > 1000]
    print(nombres if nombres else "Ninguno supera 1000.")

def mostrar_producto_info():
    print("\nMAPEO PRODUCTO -> VALOR:")
    info = {i["producto"]: i["unidades"] * i["precio"] for i in ventas}
    for nombre, valor in info.items():
        print(f"{nombre}: {valor}")

def mostrar_ranking_premium():
    print("\nRANKING PREMIUM (PRECIO > 50):")
    ranking = {i["producto"]: i["unidades"] * i["precio"] for i in ventas if i["precio"] > 50}
    ordenado = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
    for nombre, valor in ordenado:
        print(f"{nombre}: {valor}")

def mostrar_set_comp():
    print("\nPRODUCTOS BARATOS (PRECIO <= 50):")
    baratos = {i["producto"] for i in ventas if i["precio"] <= 50}
    print(baratos)

def mostrar_resumen():
    print("\nRESUMEN FINAL:")
    valor_por_producto = [i["unidades"] * i["precio"] for i in ventas]
    gran_total = sum(valor_por_producto)
    resumen = {i["producto"]: i["unidades"] * i["precio"] for i in ventas}
    print(f"Gran total: {gran_total}")
    print("\nDetalle:")
    for producto, valor in resumen.items():
        print(f"  {producto}: {valor}")

def menu():
    while True:
        print("\nMENU DE VENTAS")
        print("1. Ver valor total por producto")
        print("2. Productos con valor > 1000")
        print("3. Ver mapeo producto -> valor")
        print("4. Ranking premium (precio > 50)")
        print("5. Productos baratos (set)")
        print("6. Resumen final")
        print("7. Salir")
        
        opcion = input("Selecciona una opcion: ")
        
        if opcion == "1":
            mostrar_valor_total()
        elif opcion == "2":
            mostrar_productos_mayor_1000()
        elif opcion == "3":
            mostrar_producto_info()
        elif opcion == "4":
            mostrar_ranking_premium()
        elif opcion == "5":
            mostrar_set_comp()
        elif opcion == "6":
            mostrar_resumen()
        elif opcion == "7":
            print("Cerrando...bro")
            break
        else:
            print("Opcion no valida.")

menu()
