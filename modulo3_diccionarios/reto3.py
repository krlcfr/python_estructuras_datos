ventas_por_region = {
    "Norte": {"Q1": 15000, "Q2": 18000, "Q3": 22000, "Q4": 24000},
    "Sur": {"Q1": 12000, "Q2": 16000, "Q3": 19000, "Q4": 21000},
    "Este": {"Q1": 20000, "Q2": 22000, "Q3": 25000, "Q4": 28000},
    "Oeste": {"Q1": 10000, "Q2": 14000, "Q3": 17000, "Q4": 19000}
}

def calcular_totales_regionales():
    return {region: sum(ventas.values()) for region, ventas in ventas_por_region.items()}

def region_mayor_venta():
    return max(ventas_por_region, key=lambda k: sum(ventas_por_region[k].values()))

def ventas_por_trimestre():
    trimestres = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}
    for region, qs in ventas_por_region.items():
        for q, monto in qs.items():
            trimestres[q] += monto
    return trimestres

def calcular_porcentajes():
    totales = calcular_totales_regionales()
    gran_total = sum(totales.values())
    return {region: (total / gran_total) * 100 for region, total in totales.items()}

def mostrar_totales():
    print("\nTOTALES ANUALES POR REGION:")
    totales = calcular_totales_regionales()
    for region, total in totales.items():
        print(f"{region}: {total}")

def mostrar_region_max():
    print("\nREGION CON MAYORES VENTAS:")
    region = region_mayor_venta()
    totales = calcular_totales_regionales()
    print(f"{region}: {totales[region]}")

def mostrar_ventas_trimestrales():
    print("\nVENTAS ACUMULADAS POR TRIMESTRE:")
    trimestres = ventas_por_trimestre()
    for q, monto in trimestres.items():
        print(f"{q}: {monto}")

def mostrar_porcentajes():
    print("\nPORCENTAJE DE VENTAS POR REGION:")
    porcentajes = calcular_porcentajes()
    for region, pct in porcentajes.items():
        print(f"{region}: {pct:.2f}%")

def mostrar_reporte_ordenado():
    print("\nREPORTE ORDENADO DE MAYOR A MENOR:")
    totales = calcular_totales_regionales()
    reporte = sorted(totales.items(), key=lambda x: x[1], reverse=True)
    for region, total in reporte:
        print(f"{region}: {total}")

def menu():
    while True:
        print("\nANALISIS DE VENTAS TRIMESTRALES")
        print("1. Ventas totales anuales por region")
        print("2. Region con mayores ventas")
        print("3. Ventas acumuladas por trimestre")
        print("4. Porcentajes por region")
        print("5. Reporte de mayor a menor")
        print("6. Salir")
        
        opcion = input("Selecciona una opcion: ")
        
        if opcion == "1":
            mostrar_totales()
        elif opcion == "2":
            mostrar_region_max()
        elif opcion == "3":
            mostrar_ventas_trimestrales()
        elif opcion == "4":
            mostrar_porcentajes()
        elif opcion == "5":
            mostrar_reporte_ordenado()
        elif opcion == "6":
            print("Cerrando...bro")
            break
        else:
            print("Opcion no valida.")

menu()
