tienda_centro = {"Laptop", "Mouse", "Teclado", "Monitor", "Cable USB"}
tienda_norte = {"Mouse", "Teclado", "Silla Ergonomica", "Lampara de Escritorio"}
tienda_sur = {"Laptop", "Silla Ergonomica", "Cable HDMI", "Monitor", "Impresora"}

usuario1 = {"Accion", "Comedia", "Drama", "Ciencia Ficcion"}
usuario2 = {"Comedia", "Terror", "Romance", "Ciencia Ficcion"}
usuario3 = {"Drama", "Romance", "Accion", "Terror"}

def mostrar_catalogo_completo():
    print("\nTODO LO QUE VENDEN (UNION):")
    catalogo = tienda_centro.union(tienda_norte, tienda_sur)
    print(catalogo)

def mostrar_productos_comunes():
    print("\nLO QUE COMPARTEN TODAS (INTERSECCION):")
    comunes = tienda_centro.intersection(tienda_norte, tienda_sur)
    print(comunes if comunes else "Nada en comun entre las 3.")

def mostrar_exclusivos():
    print("\nQUE TIENE CADA UNA SOLO PARA ELLA:")
    exc_centro = tienda_centro.difference(tienda_norte, tienda_sur)
    exc_norte = tienda_norte.difference(tienda_centro, tienda_sur)
    exc_sur = tienda_sur.difference(tienda_centro, tienda_norte)
    print(f"Centro: {exc_centro}")
    print(f"Norte: {exc_norte}")
    print(f"Sur: {exc_sur}")

def verificar_solapamientos():
    print("\nSI SE PISAN ENTRE ELLAS:")
    print(f"Centro y Norte: {'No se pisan' if tienda_centro.isdisjoint(tienda_norte) else 'Si se pisan'}")
    print(f"Centro y Sur: {'No se pisan' if tienda_centro.isdisjoint(tienda_sur) else 'Si se pisan'}")
    print(f"Norte y Sur: {'No se pisan' if tienda_norte.isdisjoint(tienda_sur) else 'Si se pisan'}")

def mostrar_comunes_usuarios():
    print("\nGENEROS QUE LES GUSTAN A VARIOS (&):")
    print(f"Usuario1 y Usuario2: {usuario1 & usuario2}")
    print(f"Usuario1 y Usuario3: {usuario1 & usuario3}")

def mostrar_universo_generos():
    print("\nTODOS LOS GENEROS JUNTOS (|):")
    print(usuario1 | usuario2 | usuario3)

def mostrar_exclusivos_usuario():
    print("\nGENEROS SOLO DE UN USUARIO (-):")
    print(f"Solo Usuario1 (no Usuario2): {usuario1 - usuario2}")
    print(f"Solo Usuario2 (no Usuario3): {usuario2 - usuario3}")

def mostrar_diferencia_simetrica():
    print("\nGENEROS QUE NO COMPARTEN (^):")
    print(f"Usuario1 vs Usuario2: {usuario1 ^ usuario2}")

def verificar_subconjuntos():
    print("\nSI UNO ESTA DENTRO DE OTRO (<=):")
    universo = usuario1 | usuario2 | usuario3
    print(f"Usuario1 esta en el universo: {usuario1 <= universo}")
    print(f"Usuario2 esta en Usuario1: {usuario2 <= usuario1}")
    print(f"Usuario3 esta en el universo: {usuario3 <= universo}")

def mostrar_resumen_final():
    print("\nRESUMEN FINAL:")
    catalogo = tienda_centro.union(tienda_norte, tienda_sur)
    universo_generos = usuario1 | usuario2 | usuario3
    print(f"Total productos: {len(catalogo)}")
    print(f"Total generos: {len(universo_generos)}")
    print(f"Tiendas que se pisan: Centro-Norte, Centro-Sur")
    print(f"Generos que mas se repiten: {usuario1 & usuario2 & usuario3}")

def menu():
    while True:
        print("\nMENU DE TIENDAS Y PELIS")
        print("1. Ver todo lo que venden")
        print("2. Ver que comparten todas")
        print("3. Ver que tiene cada una sola")
        print("4. Ver si se pisan entre ellas")
        print("5. Generos que les gustan a varios")
        print("6. Ver todos los generos juntos")
        print("7. Generos solo de un usuario")
        print("8. Generos que no comparten")
        print("9. Ver si uno esta dentro de otro")
        print("10. Resumen final")
        print("11. Salir")
        
        opcion = input("Selecciona una opcion: ")
        
        if opcion == "1":
            mostrar_catalogo_completo()
        elif opcion == "2":
            mostrar_productos_comunes()
        elif opcion == "3":
            mostrar_exclusivos()
        elif opcion == "4":
            verificar_solapamientos()
        elif opcion == "5":
            mostrar_comunes_usuarios()
        elif opcion == "6":
            mostrar_universo_generos()
        elif opcion == "7":
            mostrar_exclusivos_usuario()
        elif opcion == "8":
            mostrar_diferencia_simetrica()
        elif opcion == "9":
            verificar_subconjuntos()
        elif opcion == "10":
            mostrar_resumen_final()
        elif opcion == "11":
            print("Cerrando...bro")
            break
        else:
            print("Opcion no valida.")

menu()
