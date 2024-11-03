# Fonction pour calculer la moyenne des notes
def calculer_moyenne(notes):
    return sum(notes) / len(notes) if notes else 0

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

# Affichage des moyennes des élèves
print("\nMoyennes des élèves :")
for nom, moyenne in eleves.items():
    print(f"{nom} : {moyenne:.2f}")

