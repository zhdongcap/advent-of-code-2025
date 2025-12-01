import os

def solve():
    # Le fichier est dans le même dossier que le script
    file_path = os.path.join(os.path.dirname(__file__), 'question.txt')
    
    try:
        with open(file_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Erreur: Le fichier {file_path} est introuvable.")
        return
    
    # Séparer la description de l'input
    # On cherche la phrase "and Input it's here"
    separator = "and Input it's here"
    if separator not in content:
        print("Erreur: Impossible de trouver le début des données (phrase 'and Input it's here' manquante).")
        return

    input_part = content.split(separator)[1].strip()
    lines = input_part.splitlines()
    
    # État initial
    position = 50
    zero_hits_part1 = 0
    zero_hits_part2 = 0
    
    print(f"Position de départ: {position}")
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Parsing de la ligne (ex: R45 ou L42)
        direction = line[0].upper()
        try:
            amount = int(line[1:])
        except ValueError:
            print(f"Ligne ignorée (format incorrect): {line}")
            continue
            
        # Calcul pour la Partie 2 (Passages par 0)
        # Distance jusqu'au prochain 0 dans la direction donnée
        dist_to_zero = 0
        if direction == 'R':
            # Vers la droite : distance = 100 - position (si pos=0, dist=100)
            dist_to_zero = 100 - position if position != 0 else 100
        elif direction == 'L':
            # Vers la gauche : distance = position (si pos=0, dist=100)
            dist_to_zero = position if position != 0 else 100
            
        if amount >= dist_to_zero:
            # On atteint au moins une fois 0
            # Le premier 0 est atteint après dist_to_zero
            # Ensuite, chaque 100 unités supplémentaires donne un autre 0
            remaining = amount - dist_to_zero
            hits = 1 + (remaining // 100)
            zero_hits_part2 += hits

        # Mise à jour de la position (Partie 1 & État courant)
        if direction == 'R':
            position = (position + amount) % 100
        elif direction == 'L':
            position = (position - amount) % 100
        
        # Vérification si on s'arrête sur 0 (Partie 1)
        if position == 0:
            zero_hits_part1 += 1
            
    print(f"Partie 1 - Arrêts sur 0 : {zero_hits_part1}")
    print(f"Partie 2 - Passages par 0 (Total) : {zero_hits_part2}")

if __name__ == "__main__":
    solve()
