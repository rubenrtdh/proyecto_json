import json

# Ejercicio 1: Listar álbumes de un artista
def listar_albumes_artista(doc, nombre_artista):
    resultados = []
    for artista in doc['artistas']:
        if artista['nombre'].lower() == nombre_artista.lower():
            for album in artista['albumes']:
                info_album = {
                    'titulo': album['titulo'],
                    'año': album['año'],
                    'canciones': [
                        f"{c['titulo']} ({c['duracion']})" 
                        for c in album['canciones']
                    ]
                }
                resultados.append(info_album)
            return resultados
    return None
# Ejercicio 2: Contar canciones y álbumes
def contar_datos(doc):
    conteo_canciones = {}
    conteo_generos = {}
    
    for artista in doc['artistas']:
        total_canciones = sum(len(a['canciones']) for a in artista['albumes'])
        conteo_canciones[artista['nombre']] = total_canciones
        
        for album in artista['albumes']:
            conteo_generos[album['genero']] = conteo_generos.get(album['genero'], 0) + 1
    
    return conteo_canciones, conteo_generos
