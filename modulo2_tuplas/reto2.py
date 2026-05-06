catalogo = (
    ("Matrix", "Wachowski", 1999, 8.7),
    ("Inception", "Nolan", 2010, 8.8),
    ("Interstellar", "Nolan", 2014, 8.6)
)

def mostrar_catalogo():
    primera, *resto = catalogo
    
    print("\nPRIMERA PELICULA:")
    titulo, director, año, nota = primera
    print(f"Peli: {titulo:<12} | Dir: {director:<10} | Anio: {año} | Nota: {nota}")
    
    print("\nRESTO DEL CATALOGO:")
    for titulo, director, año, nota in resto:
        print(f"Peli: {titulo:<12} | Dir: {director:<10} | Anio: {año} | Nota: {nota}")

def añadir_pelicula():
    global catalogo
    titulo = input("Nombre de la peli: ")
    director = input("Director: ")
    año = int(input("Año: "))
    nota = float(input("Puntuacion (0-10): "))
    nueva_peli = (titulo, director, año, nota)
    catalogo = catalogo + (nueva_peli,)
    print(f"{titulo} añadida al catalogo!")

def buscar_por_director(director):
    return tuple(p for p in catalogo if p[1].lower() == director.lower())

def obtener_estadisticas():
    if not catalogo:
        return None
    notas = [p[3] for p in catalogo]
    return (min(notas), max(notas), sum(notas) / len(notas))

def menu():
    while True:
        print("\nGESTION DE CATALOGO")
        print("1. Mostrar catalogo")
        print("2. Añadir pelicula")
        print("3. Buscar por director")
        print("4. Ver estadisticas")
        print("5. Salir")
        
        opcion = input("Selecciona una opcion: ")
        
        if opcion == "1":
            mostrar_catalogo()
        elif opcion == "2":
            añadir_pelicula()
        elif opcion == "3":
            dir_buscado = input("Que director buscas?: ")
            resultados = buscar_por_director(dir_buscado)
            if resultados:
                for p in resultados:
                    print(f"Encontrada: {p[0]} ({p[2]})")
            else:
                print("No se encontro nada de ese director.")
        elif opcion == "4":
            stats = obtener_estadisticas()
            if stats:
                min_val, max_val, prom_val = stats
                print(f"\nEstadisticas -> Min: {min_val} | Max: {max_val} | Prom: {prom_val:.2f}")
            else:
                print("Catalogo vacio.")
        elif opcion == "5":
            print("Cerrando...bro")
            break
        else:
            print("Opcion no valida.")

menu()