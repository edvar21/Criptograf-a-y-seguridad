def polibio_revertir(codigo_cifrado):
    # El alfabeto debe coincidir exactamente con el del cifrador 
    alfabeto_plano = "ABCDE" "FGHIJ" "KLMNO" "PQRST" "UVWXY"
    
    # Separamos los pares por el espacio 
    elementos = codigo_cifrado.split()
    mensaje_claro = ""
    
    for item in elementos:
        # Verificamos que sea un par de dígitos para procesar 
        if item.isdigit() and len(item) == 2:
            # Convertimos coordenadas a índices (restando 1) 
            f = int(item[0]) - 1
            c = int(item[1]) - 1
            
            # Calculamos la posición en la cadena: (fila * 5) + columna
            pos = (f * 5) + c
            mensaje_claro += alfabeto_plano[pos]
        else:
            # Si no es un par válido, se mantiene el carácter original 
            mensaje_claro += item
            
    return mensaje_claro

if __name__ == "__main__":
    print("Ingrese los pares numéricos separados por espacios:")
    entrada_cifrada = input("Código: ")
    print("Texto recuperado:", polibio_revertir(entrada_cifrada))