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
