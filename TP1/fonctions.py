def puissance(a, b):
    if not type(a) is int or not type(b) is int:
        raise TypeError("Seuls les entiers sont autorisés pour les arguments a et b")
    
    resultat = a ** b
    return resultat
