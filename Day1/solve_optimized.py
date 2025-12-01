import os
import re

def solve():
    # Lecture du fichier robuste
    file_path = os.path.join(os.path.dirname(__file__), 'question.txt')
    with open(file_path, 'r') as f:
        content = f.read()
        # Extraction de la partie Input si nécessaire
        if "and Input it's here" in content:
            content = content.split("and Input it's here")[1]

    # Parsing ultra-rapide avec Regex (générateur)
    # Trouve tous les couples (Lettre, Chiffre)
    # re.findall avec groupes renvoie une liste de tuples [('R', '45'), ('L', '10')...]
    ops = ((m[0], int(m[1])) for m in re.findall(r'([RL])(\d+)', content))

    # On utilise une position absolue (pas de modulo 100 ici)
    # 0, 100, 200, -100... sont tous des "0" sur le cadran.
    abs_pos = 50
    p1, p2 = 0, 0

    for direction, val in ops:
        if direction == 'R':
            # Vers la droite (positif)
            # On compte combien de multiples de 100 sont dans l'intervalle (pos, pos + val]
            # Formule: floor(fin / 100) - floor(debut / 100)
            p2 += (abs_pos + val) // 100 - abs_pos // 100
            abs_pos += val
        else:
            # Vers la gauche (négatif)
            # On compte combien de multiples de 100 sont dans l'intervalle [pos - val, pos)
            # Attention aux bornes pour les nombres négatifs
            p2 += (abs_pos - 1) // 100 - (abs_pos - val - 1) // 100
            abs_pos -= val

        # Partie 1 : On vérifie juste si la position finale est un multiple de 100
        if abs_pos % 100 == 0:
            p1 += 1

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")

if __name__ == "__main__":
    solve()
