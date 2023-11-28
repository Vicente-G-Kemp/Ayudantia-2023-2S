import re

def limpiar_archivo(nombre_archivo_entrada, nombre_archivo_salida):
    with open(nombre_archivo_entrada, 'r', encoding='utf-8') as archivo_entrada:
        contenido = archivo_entrada.read()
        contenido_limpiado = re.sub(r'[^a-zA-Z0-9\s(),]', '', contenido)

    with open(nombre_archivo_salida, 'w', encoding='utf-8') as archivo_salida:
        archivo_salida.write(contenido_limpiado)

limpiar_archivo('../outhadoop/part-00000', 'new_output.txt')

