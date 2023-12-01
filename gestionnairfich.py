import json

# Charger la base de données depuis le fichier JSON
with open('gestionnairetache.json') as json_data:
    tasks = json.load(json_data)

def charger_base_de_donnees():
    # Fonction pour charger la base de données depuis le fichier JSON
    with open('gestionnairetache.json', 'r') as f:
        return json.load(f)

def sauvegarder_base_de_donnees(tasks):
    # Fonction pour sauvegarder la base de données dans le fichier JSON
    with open('gestionnairetache.json', 'w') as f:
        json.dump(tasks, f, indent=2)

def afficher_taches():
    # Fonction pour afficher la liste des tâches
    tasks = charger_base_de_donnees()
    print("Liste des tâches :")
    for index, tache in enumerate(tasks["tasks"], start=1):
        print(f"{index}. Nom : {tache['nom']}, Description : {tache['description']}, "
              f"Date d'échéance : {tache['date_d_echeance']}, État : {tache['etat']}")

def ajouter_tache():
    # Fonction pour ajouter une nouvelle tâche
    tasks = charger_base_de_donnees()
    nom = input("Nom de la tâche : ")
    description = input("Description de la tâche : ")
    date_d_echeance_str = input("Date d'échéance (format YYYY-MM-DD) : ")
    etat = input("État initial de la tâche : ")

    nouvelle_tache = {
        "nom": nom,
        "description": description,
        "date_d_echeance": date_d_echeance_str,
        "etat": etat
    }

    tasks["tasks"].append(nouvelle_tache)
    sauvegarder_base_de_donnees(tasks)
    print("Nouvelle tâche ajoutée avec succès.")

def supprimer_tache():
    # Fonction pour supprimer une tâche
    tasks = charger_base_de_donnees()
    print("Liste des tâches actuelles :")
    for index, tache in enumerate(tasks["tasks"], start=1):
        print(f"{index}. {tache['nom']}")

    nom_tache_a_supprimer = input("Entrez le nom de la tâche à supprimer : ")

    tache_trouvee = None
    for tache in tasks["tasks"]:
        if tache["nom"] == nom_tache_a_supprimer:
            tache_trouvee = tache
            break

    if tache_trouvee:
        tasks["tasks"].remove(tache_trouvee)
        sauvegarder_base_de_donnees(tasks)
        print(f"Tâche '{nom_tache_a_supprimer}' supprimée avec succès.")
    else:
        print(f"Tâche '{nom_tache_a_supprimer}' non trouvée.")

def modifier_tache():
    # Fonction pour modifier une tâche
    tasks = charger_base_de_donnees()
    print("Liste des tâches actuelles :")
    for index, tache in enumerate(tasks["tasks"], start=1):
        print(f"{index}. {tache['nom']}")

    nom_tache_a_modifier = input("Entrez le nom de la tâche à modifier : ")

    tache_a_modifier = None
    for tache in tasks["tasks"]:
        if tache["nom"] == nom_tache_a_modifier:
            tache_a_modifier = tache
            break

    if tache_a_modifier:
        nouvelle_nom = input("Nouveau nom de la tâche : ")
        nouvelle_description = input("Nouvelle description de la tâche : ")
        nouvelle_date_d_echeance_str = input("Nouvelle date d'échéance (format YYYY-MM-DD) : ")
        nouvel_etat = input("Nouvel état de la tâche : ")

        tache_a_modifier["nom"] = nouvelle_nom
        tache_a_modifier["description"] = nouvelle_description
        tache_a_modifier["date_d_echeance"] = nouvelle_date_d_echeance_str
        tache_a_modifier["etat"] = nouvel_etat

        sauvegarder_base_de_donnees(tasks)
        print(f"Tâche '{nom_tache_a_modifier}' modifiée avec succès.")
    else:
        print(f"Tâche '{nom_tache_a_modifier}' non trouvée.")

def menu():
    # Fonction principale pour afficher le menu et gérer les choix de l'utilisateur
    while True:
        print("\nMenu :")
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Supprimer une tâche")
        print("4. Modifier une tâche")
        print("5. Quitter")

        choix = input("Veuillez choisir une option (1-5) : ")

        if choix == "1":
            afficher_taches()
        elif choix == "2":
            ajouter_tache()
        elif choix == "3":
            supprimer_tache()
        elif choix == "4":
            modifier_tache()
        elif choix == "5":
            print("Programme terminé.")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

# Appeler la fonction menu pour exécuter le programme
menu()
