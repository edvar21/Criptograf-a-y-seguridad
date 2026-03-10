def polibio_encriptar(mensaje):
    mensaje = mensaje.upper().replace(" ", "")
   
    cuadrícula = "ABCDE" "FGHIJ" "KLMNO" "PQRST" "UVWXY"
    
    salida = []
    
    for caracter in mensaje:
        if caracter in cuadrícula:
            indice = cuadrícula.index(caracter)
            
            fila = (indice // 5) + 1
            columna = (indice % 5) + 1
            
            salida.append(f"{fila}{columna}")
        else:
            salida.append(caracter)
             
    return " ".join(salida)

if __name__ == "__main__":
    entrada = input("Texto a cifrar: ")
    print("Resultado del cifrado:", polibio_encriptar(entrada))