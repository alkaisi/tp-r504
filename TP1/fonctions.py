def puissance(a, b):
    # Vérifie que les arguments a et b sont des entiers
    if not type(a) is int or not type(b) is int:
        raise TypeError("Seuls les entiers sont autorisés pour les arguments a et b")

    # Initialise la variable résultat à 1
    resultat = 1

    # Gère le cas où l'exposant (b) est négatif
    if b < 0:
        # Prend l'inverse de a pour gérer l'exposant négatif
        a = 1 / a
        # Transforme b en positif pour gérer l'exposant négatif
        b = -b

    # Utilise une boucle for pour calculer la puissance de a à la puissance b
    for _ in range(b):
        resultat *= a

    # Retourne le résultat du calcul de la puissance
    return resultat
