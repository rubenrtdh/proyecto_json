import json

def cargar_datos():
    with open('musica.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# 1. Listar álbumes de un artista
def listar_albumes_artista(doc):
    nombre = input("Nombre del artista: ").strip()
    artistas = [a for a in doc['artistas'] if a['nombre'].lower() == nombre.lower()]
    
    if not artistas:
        print("Artista no encontrado")
        return
    
    print(f"\nÁlbumes de {nombre}:")
    print(f"{'Álbum':<40} {'Año':<10}")  # Encabezados de la tabla
    print("-" * 50)  # Línea divisoria
    for album in artistas[0]['albumes']:
        print(f"{album['titulo']:<40} {album['año']:<10}")  # Formato de tabla

# 2. Contar información
def contar_datos(doc):
    conteo_canciones = {}
    conteo_generos = {}
    
    for artista in doc['artistas']:
        total_canciones = sum(len(album['canciones']) for album in artista['albumes'])
        conteo_canciones[artista['nombre']] = total_canciones
        
        for album in artista['albumes']:
            genero = album['genero']
            if genero not in conteo_generos:
                conteo_generos[genero] = 0
            conteo_generos[genero] += 1
    
    # Mostrar canciones por artista
    print("\nCanciones por artista:")
    print(f"{'Artista':<30} {'Canciones':<10}")  # Encabezados de la tabla
    print("-" * 40)  # Línea divisoria
    for artista, total in conteo_canciones.items():
        print(f"{artista:<30} {total:<10}")  # Formato de tabla
    
    # Mostrar álbumes por género
    print("\nÁlbumes por género:")
    print(f"{'Género':<30} {'Álbumes':<10}")  # Encabezados de la tabla
    print("-" * 40)  # Línea divisoria
    for genero, total in conteo_generos.items():
        print(f"{genero:<30} {total:<10}")  # Formato de tabla

# 3. Filtrar álbumes por género
def filtrar_por_genero(doc):
    genero = input("Género musical: ").strip()
    resultados = []
    
    for artista in doc['artistas']:
        for album in artista['albumes']:
            if album['genero'].lower() == genero.lower():
                resultados.append((artista['nombre'], album['titulo'], album['año']))
    
    if resultados:
        print(f"\nÁlbumes en el género '{genero}':")
        print(f"{'Artista':<30} {'Álbum':<30} {'Año':<10}")  # Encabezados de la tabla
        print("-" * 70)  # Línea divisoria
        for artista, titulo, año in resultados:
            print(f"{artista:<30} {titulo:<30} {año:<10}")  # Formato de tabla
    else:
        print("No hay álbumes en este género")

# 4. Buscar canción
def buscar_cancion(doc):
    titulo = input("Título de la canción: ").strip()
    resultados = []
    
    for artista in doc['artistas']:
        for album in artista['albumes']:
            for cancion in album['canciones']:
                if cancion['titulo'].lower() == titulo.lower():
                    resultados.append({
                        'artista': artista['nombre'],
                        'album': album['titulo'],
                        'rating': cancion['rating']
                    })
    
    if resultados:
        print("\nInformación de la canción:")
        print(f"{'Artista':<30} {'Álbum':<30} {'Rating':<10}")  # Encabezados de la tabla
        print("-" * 70)  # Línea divisoria
        for res in resultados:
            print(f"{res['artista']:<30} {res['album']:<30} {res['rating']:<10}")  # Formato de tabla
    else:
        print(f"\n[ERROR] No se encontró la canción '{titulo}'.")

# 5. Rankings
def generar_rankings(doc):
    # Ranking artistas
    ranking_artistas = []
    for artista in doc['artistas']:
        total = sum(len(album['canciones']) for album in artista['albumes'])
        ranking_artistas.append({'nombre': artista['nombre'], 'total': total})
    
    # Ordenar manualmente
    for i in range(len(ranking_artistas)):
        for j in range(len(ranking_artistas)-1):
            if ranking_artistas[j]['total'] < ranking_artistas[j+1]['total']:
                ranking_artistas[j], ranking_artistas[j+1] = ranking_artistas[j+1], ranking_artistas[j]
    
    # Ranking canciones
    ranking_canciones = []
    for artista in doc['artistas']:
        for album in artista['albumes']:
            for cancion in album['canciones']:
                ranking_canciones.append({
                    'nombre': f"{cancion['titulo']} - {artista['nombre']}",
                    'rating': cancion['rating']
                })
    
    # Ordenar manualmente
    for i in range(len(ranking_canciones)):
        for j in range(len(ranking_canciones)-1):
            if ranking_canciones[j]['rating'] < ranking_canciones[j+1]['rating']:
                ranking_canciones[j], ranking_canciones[j+1] = ranking_canciones[j+1], ranking_canciones[j]
    
    # Tabla de artistas
    print("\nTop 5 artistas con más canciones:")
    print(f"{'Pos':<5} {'Artista':<30} {'Canciones':<10}")  # Encabezados de la tabla
    print("-" * 45)  # Línea divisoria
    for i in range(5):
        if i < len(ranking_artistas):
            print(f"{i+1:<5} {ranking_artistas[i]['nombre']:<30} {ranking_artistas[i]['total']:<10}")  # Formato de tabla
    
    # Tabla de canciones
    print("\nTop 5 canciones mejor calificadas:")
    print(f"{'Pos':<5} {'Canción':<40} {'Rating':<10}")  # Encabezados de la tabla
    print("-" * 60)  # Línea divisoria
    for i in range(5):
        if i < len(ranking_canciones):
            print(f"{i+1:<5} {ranking_canciones[i]['nombre']:<40} {ranking_canciones[i]['rating']:<10}")  # Formato de tabla
