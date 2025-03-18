from funciones import *

def menu():
    print("\n--- MENÚ ---")
    print("1. Listar álbumes de un artista")
    print("2. Contar canciones y álbumes")
    print("3. Filtrar álbumes por género")
    print("4. Buscar canción")
    print("5. Ver rankings")
    print("6. Salir")

def main():
    doc = cargar_datos()
    ejecutar = True
    
    while ejecutar:
        menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            listar_albumes_artista(doc)
        elif opcion == "2":
            contar_datos(doc)
        elif opcion == "3":
            filtrar_por_genero(doc)
        elif opcion == "4":
            buscar_cancion(doc)
        elif opcion == "5":
            generar_rankings(doc)
        elif opcion == "6":
            print("¡Hasta luego!")
            ejecutar = False
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
