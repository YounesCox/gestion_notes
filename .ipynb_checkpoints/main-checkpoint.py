from models.gestion_notes import GestionNotes
from menus.menu_principal import afficher_menu_principal
from menus.menu_gestion import afficher_sous_menu_gestion, creer_fichier_par_defaut
from modules.statistiques import afficher_tableau_bord_statistique

def main():
    gestion_notes = GestionNotes()
    
    while True:
        afficher_menu_principal()
        choix = input("Votre choix: ").strip()
        
        if choix == '1':
            afficher_sous_menu_gestion()
            sous_choix = input("→ ").strip()
            if sous_choix == '1':
                creer_fichier_par_defaut(gestion_notes)
        
        elif choix == '2':
            afficher_tableau_bord_statistique(gestion_notes)
        
        elif choix == '7':
            print("👋 Au revoir !")
            break
        else:
            print("❌ Choix invalide")

if __name__ == "__main__":
    main()
