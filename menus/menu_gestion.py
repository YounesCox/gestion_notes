import pandas as pd

def creer_fichier_par_defaut(gestion_notes):
    notes_par_defaut = [
        {"Nom": "Safae", "Note": 15}, {"Nom": "Ahmed", "Note": 18},
        {"Nom": "Marie", "Note": 12}, {"Nom": "Pierre", "Note": 16}
    ]
    gestion_notes.df_notes = pd.DataFrame(notes_par_defaut)
    gestion_notes.sauvegarder_notes()
    print("✓ Fichier créé avec succès")

def afficher_sous_menu_gestion():
    print("\n📝 GESTION DES NOTES")
    print("1. Créer un fichier par défaut")
    print("2. Ajouter une note")
    print("3. Ajouter plusieurs notes")
    print("4. Afficher toutes les notes")
    print("5. Retour")
