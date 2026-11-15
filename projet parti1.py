taches = []  

def afficher_menu():
    print("\n=== GESTION DES TACHES ===")
    print("1. Ajouter une tâche   2. Afficher   3. Rechercher   0. Quitter")

def ajouter_tache():
    titre = input("Titre de la tâche : ").strip()
    if titre == "":
        print("Erreur : le titre ne peut pas être vide.")
        return
    taches.append({"titre": titre, "faite": False})
    print("Tâche ajoutée avec succès.")


def afficher_taches():
    if len(taches) == 0:
        print("Aucune tâche pour le moment.")
        return
    for i in range(len(taches)):
        print(f"{i + 1} - {taches[i]['titre']}")


def rechercher_tache():
    saisie = input("Numéro de la tâche : ").strip()
    if not saisie.isdigit():
        print("Erreur : veuillez saisir un numéro valide.")
        return
    numero = int(saisie)
    if numero < 1 or numero > len(taches):
        print("Aucune tâche avec ce numéro.")
        return
    print(f"Tâche {numero} : {taches[numero - 1]['titre']}")


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
            print("Choix invalide, veuillez réessayer.")


if __name__ == "__main__":
    main()
