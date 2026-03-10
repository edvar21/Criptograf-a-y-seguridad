from collections import defaultdict

def analyze_kasiski(cipher):
    raw = "".join(filter(str.isalpha, cipher.upper()))
    
    seq_map = defaultdict(list)
    for i in range(len(raw) - 2):
        seq_map[raw[i:i+3]].append(i)

    repeats = {k: v for k, v in seq_map.items() if len(v) > 1}
    
    if not repeats:
        return print("Sin patrones repetidos.")

    diffs = []
    for pos in repeats.values():
        diffs.extend([pos[i+1] - pos[i] for i in range(len(pos)-1)])

    factor_counts = defaultdict(int)
    for d in diffs:
        for i in range(2, 21):
            if d % i == 0:
                factor_counts[i] += 1

    print("Candidatos de longitud de clave:")
    sorted_factors = sorted(factor_counts.items(), key=lambda x: x[1], reverse=True)
    for length, freq in sorted_factors[:5]:
        print(f"Longitud {length}: encontrada {freq} veces")

analyze_kasiski(input("Texto cifrado: "))