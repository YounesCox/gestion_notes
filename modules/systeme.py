import os
from datetime import datetime

def afficher_infos_systeme():
    """Affiche les informations système de base."""
    print("\n🖥️ INFORMATIONS SYSTÈME")
    print("-" * 40)
    print(f"Système d’exploitation : {os.name}")
    print(f"Répertoire courant : {os.getcwd()}")
    print(f"Heure actuelle : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("-" * 40)

def sauvegarde_automatique(gestion_notes):
    """Effectue une sauvegarde automatique du fichier des notes."""
    if gestion_notes.df_notes.empty:
        print("📭 Aucune donnée à sauvegarder.")
        return
    
    nom_sauvegarde = f"sauvegarde_notes_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
    try:
        gestion_notes.df_notes.to_csv(nom_sauvegarde, index=False)
        print(f"✅ Sauvegarde automatique effectuée → {nom_sauvegarde}")
    except Exception as e:
        print(f"❌ Erreur de sauvegarde : {e}")
