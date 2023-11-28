import json
import re

def texto_a_json(texto):
    datos = {}
    lineas = texto.strip().split('\n')
    
    for linea in lineas:
        elementos = linea.split('\t')
        
        palabra = elementos[0].strip()

        datos[palabra] = []

        for frecuencia in elementos[1:]:
            matches = re.findall(r'\((\d+),\s*(\d+)\)', frecuencia)
            for match in matches:
                documento, count = map(int, match)
                datos[palabra].append({
                    "Documento": documento,
                    "Frecuencia": count,
                    "url": "https://wikipedia.org/wiki/"+ str(documento)
                })

    return datos

def main():
    with open('new_output.txt', 'r') as archivo:
        contenido = archivo.read()

    datos_json = texto_a_json(contenido)

    print(json.dumps(datos_json, indent=2))

    with open('resultado.json', 'w') as resultado_file:
        json.dump(datos_json, resultado_file, indent=2)

if __name__ == "__main__":
    main()

