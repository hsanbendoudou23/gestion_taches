# Application Python de gestion des taches
# Projet - Outils collaboratifs avec Git / GitHub

taches = []


def ajouter_tache():
    titre = input("Titre de la tache : ").strip()

    if titre == "":
        print("Erreur : le titre ne peut pas etre vide.")
    else:
        taches.append(titre)
        print("Tache ajoutee avec succes.")


def afficher_taches():
    if len(taches) == 0:
        print("Aucune tache dans la liste.")
    else:
        print("\n--- LISTE DES TACHES ---")
        for numero, titre in enumerate(taches, start=1):
            print(f"{numero}. {titre}")


def rechercher_tache():
    mot_cle = input("Mot-cle a rechercher : ").strip()

    if mot_cle == "":
        print("Veuillez saisir un mot-cle.")
        return

    resultats = []
    for numero, titre in enumerate(taches, start=1):
        if mot_cle.lower() in titre.lower():
            resultats.append((numero, titre))

    if len(resultats) == 0:
        print("Aucune tache correspondante.")
    else:
        print("\n--- RESULTATS DE LA RECHERCHE ---")
        for numero, titre in resultats:
            print(f"{numero}. {titre}")


def afficher_menu():
    print("\n=== GESTION DES TACHES ===")
    print("1. Ajouter une tache")
    print("2. Afficher les taches")
    print("3. Rechercher une tache")
    print("0. Quitter")


def main():
    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()

        if choix == "1":
            ajouter_tache()
        elif choix == "2":
            afficher_taches()
        elif choix == "3":
            rechercher_tache()
        elif choix == "0":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez choisir 1, 2, 3 ou 0.")


if __name__ == "__main__":
    main()

# Amelioration : les recherches ignorent les majuscules et minuscules.
