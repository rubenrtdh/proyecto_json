import json
from funciones import *

def cargar_json():
    with open('musica.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def menu():
    print("\n--- MENÚ ---")
    print("1. Listar álbumes de un artista")
    print("2. Contar canciones y álbumes")
    print("3. Filtrar álbumes por género")
    print("4. Buscar canción")
    print("5. Ver rankings")
    print("6. Salir")

def main():
    doc = cargar_json()
    ejecutar = True  # Flag para controlar el bucle
    
    while ejecutar:
        menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del artista: ")
            albumes = listar_albumes_artista(doc, nombre)
            if albumes:
                print(f"\nÁlbumes de {nombre}:")
                for alb in albumes:
                    print(f"\n- {alb['titulo']} ({alb['año']})")
                    print("  Canciones:")
                    for cancion in alb['canciones']:
                        print(f"    • {cancion}")
            else:
                print("Artista no encontrado")
       elif opcion == "6":
          print("¡Hasta luego!")
          ejecutar = False  
        
      else:
          print("Opción inválida")

if __name__ == "__main__":
    main()
