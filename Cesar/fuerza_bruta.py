abc = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
mensaje_cifrado = input("Mensaje Cifrado: ")

for clave in range(len(abc)):
    mensaje_descifrado = ""
    
    for letra in mensaje_cifrado.upper():
        if letra in abc:
            indice = abc.find(letra)
            nuevo_indice = (indice - clave) % len(abc)
            mensaje_descifrado += abc[nuevo_indice]
        else:
            mensaje_descifrado += letra
    
    print(f"Clave {clave:02d}: {mensaje_descifrado}")