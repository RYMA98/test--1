def calculer_somme_controle(identifiants_boites):
    compteur_deux = 0
    compteur_trois = 0

    for identifiant in identifiants_boites:
        compteur_lettres = {}
        for lettre in identifiant:
            compteur_lettres[lettre] = compteur_lettres.get(lettre, 0) + 1

        if 2 in compteur_lettres.values():
            compteur_deux += 1
        if 3 in compteur_lettres.values():
            compteur_trois += 1

    somme_controle = compteur_deux * compteur_trois
    return somme_controle


# Exemple d'utilisation
identifiants_boites = [
    'abcdef',
    'bababc',
    'abbcde',
    'abcccd',
    'aabcdd',
    'abcdee',
    'ababab'
]

resultat = calculer_somme_controle(identifiants_boites)
print(resultat)

