import json

def buscar_palabra(json_data, palabra):
    if palabra in json_data:
        resultados = json_data[palabra]
        resultados_ordenados = sorted(resultados, key=lambda x: x['Frecuencia'], reverse=True)[:5]

        urls = [resultado['url'] for resultado in resultados_ordenados]
        return urls
    else:
        return []

def main():
    with open('../parse/resultado.json', 'r') as archivo:
        datos_json = json.load(archivo)

    palabra_buscar = input()

    resultados = buscar_palabra(datos_json, palabra_buscar)

    if resultados:
        for i, url in enumerate(resultados, 1):
            print(f"{i}. {url}")
    else:
        print(f"No hay coincidencias.")

if __name__ == "__main__":
    main()

