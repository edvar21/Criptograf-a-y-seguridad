from collections import Counter

def procesar_entrada(cadena):
    return "".join(filter(str.isalpha, cadena)).upper()

def calcular_divisores(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def ejecutar_examen_kasiski(criptograma):
    # Paso 1: Limpieza del texto
    datos = procesar_entrada(criptograma)
    largo = len(datos)
    
    # Paso 2: Localización de secuencias de 3 letras (trigramas)
    # Usamos un diccionario de listas para agrupar índices
    mapa_secuencias = {}
    for idx in range(largo - 2):
        patron = datos[idx:idx+3]
        mapa_secuencias.setdefault(patron, []).append(idx)
    
    # Filtrar solo aquellos que aparecen más de una vez
    repeticiones = {k: v for k, v in mapa_secuencias.items() if len(v) > 1}
    
    if not repeticiones:
        print("No se detectaron patrones repetidos.")
        return

    # Paso 3: Calcular distancias entre repeticiones
    intervalos = []
    for locs in repeticiones.values():
        for i in range(len(locs) - 1):
            intervalos.append(locs[i+1] - locs[i])

    # Paso 4: Análisis de frecuencias de los factores de las distancias
    # Expandimos todos los factores de cada distancia en una sola lista
    pool_de_factores = []
    for dist in intervalos:
        pool_de_factores.extend(calcular_divisores(dist))

    # Usamos Counter para obtener el conteo de frecuencias automáticamente
    frecuencias = Counter(pool_de_factores)
    
    # Ordenar por el valor de la frecuencia (el segundo elemento de la tupla)
    ranking = frecuencias.most_common(5)

    print("\nLongitud de clave probable:")
    for longitud, veces in ranking:
        print(f"    Longitud posible: {longitud} |  Numero de repeticiones: {veces}")

if __name__ == "__main__":
    entrada_usuario = input("Texto cifrado: ")
    if not entrada_usuario.strip():
        print("Error: Entrada vacía.")
    else:
        ejecutar_examen_kasiski(entrada_usuario)