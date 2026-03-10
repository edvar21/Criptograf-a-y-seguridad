def fuerza_bruta():
    abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    
    msg = input("Mensaje: ").upper()
    intercepted = input("Letra interceptada: ").upper()
    original = input("Equivalencia real: ").upper()

    try:
        offset = (abc.index(intercepted) - abc.index(original)) % len(abc)
    except ValueError:
        return "Error: Letras no encontradas en el alfabeto."

    def decrypt():
        for char in msg:
            if char in abc:
                yield abc[(abc.index(char) - offset) % len(abc)]
            else:
                yield char

    print(f"Clave detectada: {offset}")
    print("".join(decrypt()))

fuerza_bruta()