# Fonction pour calculer la moyenne des notes
def calculer_moyenne(notes):
    return sum(notes) / len(notes) if notes else 0

# Fonction pour déterminer la mention en fonction de la moyenne
def determiner_mention(moyenne):
    if moyenne >= 16:
        return "Très Bien"
    elif moyenne >= 14:
        return "Bien"
    elif moyenne >= 12:
        return "Assez Bien"
    elif moyenne >= 10:
        return "Passable"
    else:
        return "Échec"

# Initialisation de la liste pour stocker les élèves et leurs moyennes
eleves = {}

# Boucle pour entrer les données des élèves
while True:
    nom = input("Entrez le nom de l'élève (ou appuyez sur Entrée pour terminer) : ")
    if not nom:
        break

    # Demander les notes de l'élève
    notes = []
    while True:
        note = input(f"Entrez une note pour {nom} (ou appuyez sur Entrée pour terminer) : ")
        if not note:
            break
        try:
            notes.append(float(note))
        except ValueError:
            print("Veuillez entrer un nombre valide pour la note.")

    # Calcul de la moyenne
    moyenne = calculer_moyenne(notes)
    eleves[nom] = moyenne

# Affichage des moyennes et des mentions des élèves
print("\nMoyennes et Mentions des élèves :")
for nom, moyenne in eleves.items():
    mention = determiner_mention(moyenne)
    print(f"{nom} : {moyenne:.2f} - Mention : {mention}")
