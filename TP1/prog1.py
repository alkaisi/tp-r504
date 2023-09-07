print("Hello, World!")

import fonctions as f

while True:
    try:
        # Saisie d'un nombre au clavier
        v1 = int(input("Entrez un nombre v1 : "))

        # Saisie de l'exposant au clavier
        v2 = int(input("Entrez l'exposant v2 : "))

        # Calcul de la puissance
        resultat = f.puissance(v1, v2)

        # Affichage du résultat
        print(f"{v1} élevé à la puissance {v2} est : {resultat}")
    
    except ValueError:
        print("Erreur : Entrez des nombres entiers valides.")

