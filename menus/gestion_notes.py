import os
import pandas as pd
from datetime import datetime

class GestionNotes:
    def __init__(self):
        self.fichier_notes = "notes.txt"
        self.df_notes = None
        self.charger_notes()
    
    def charger_notes(self):
        if os.path.exists(self.fichier_notes):
            try:
                with open(self.fichier_notes, "r", encoding="utf-8") as f:
                    lignes = f.readlines()
                notes_data = []
                for ligne in lignes:
                    if ':' in ligne and '/' in ligne and not ligne.startswith('#'):
                        try:
                            nom = ligne.split(':')[0].strip()
                            note = float(ligne.split(':')[1].split('/')[0].strip())
                            notes_data.append({'Nom': nom, 'Note': note})
                        except (ValueError, IndexError):
                            continue
                self.df_notes = pd.DataFrame(notes_data)
            except Exception as e:
                print(f"❌ Erreur lors du chargement : {e}")
                self.df_notes = pd.DataFrame(columns=['Nom', 'Note'])
        else:
            self.df_notes = pd.DataFrame(columns=['Nom', 'Note'])
    
    def sauvegarder_notes(self):
        try:
            with open(self.fichier_notes, "w", encoding="utf-8") as f:
                f.write(f"# Fichier de notes - {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
                for _, row in self.df_notes.iterrows():
                    f.write(f"{row['Nom']} : {row['Note']}/20\n")
            return True
        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde : {e}")
            return False
