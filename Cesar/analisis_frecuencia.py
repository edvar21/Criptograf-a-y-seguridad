from collections import Counter

class AnalizadorCesar:
    def __init__(self):
        self.CHARS = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        self.MODULO = len(self.CHARS)

    def procesar(self, entrada_sucia):
        limpio = [c for c in entrada_sucia.upper() if c in self.CHARS]
        if not limpio: return None, None, entrada_sucia
        
        top_char = Counter(limpio).most_common(1)[0][0]
        
        pos_top = self.CHARS.find(top_char)
        pos_base = self.CHARS.find('E')
        offset = (pos_top - pos_base) % self.MODULO
        
        traduccion = "".join(
            self.CHARS[(self.CHARS.find(char) - offset) % self.MODULO] 
            if char in self.CHARS else char 
            for char in entrada_sucia.upper()
        )
        
        return offset, top_char, traduccion

if __name__ == "__main__":
    motor = AnalizadorCesar()
    data_input = input("Introduce el criptograma: ")
    
    key, char_max, msg_final = motor.procesar(data_input)
    
    print(f" Carácter predominante: {char_max}")
    print(f" Desplazamiento detectado: {key}")
    print(f" Texto descifrado: {msg_final}")