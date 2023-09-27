def puissance(a, b):
    # Vérifie que les arguments a et b sont des entiers
    if not type(a) is int or not type(b) is int:
        raise TypeError("Seuls les entiers sont autorisés pour les arguments a et b")

    # Gère le cas où la base est nulle (0) et l'exposant est négatif
    if a == 0 and b < 0:
        raise ValueError("La puissance de zéro à un exposant négatif n'est pas définie")

    # Initialise la variable résultat à 1
    resultat = 1

    # Gère le cas où l'exposant (b) est négatif
    if b < 0:
        a = 1 / a
        b = -b

    # Utilise une boucle for pour calculer la puissance
    for _ in range(b):
        resultat *= a

    return resultat

