import pandas as pd

def exporter_csv(gestion_notes, nom_fichier="export_notes.csv"):
    """Exporte les notes vers un fichier CSV."""
    if gestion_notes.df_notes.empty:
        print("📭 Aucune donnée à exporter.")
        return
    
    try:
        gestion_notes.df_notes.to_csv(nom_fichier, index=False, encoding='utf-8')
        print(f"✅ Exportation réussie → {nom_fichier}")
    except Exception as e:
        print(f"❌ Erreur d’exportation : {e}")

def generer_rapport_texte(gestion_notes, nom_fichier="rapport_notes.txt"):
    """Crée un rapport texte simple avec des statistiques globales."""
    if gestion_notes.df_notes.empty:
        print("📭 Aucune donnée pour le rapport.")
        return
    
    df = gestion_notes.df_notes
    moyenne = df['Note'].mean()
    minimum = df['Note'].min()
    maximum = df['Note'].max()
    
    try:
        with open(nom_fichier, "w", encoding="utf-8") as f:
            f.write("===== RAPPORT DES NOTES =====\n\n")
            for _, row in df.iterrows():
                f.write(f"{row['Nom']} : {row['Note']}/20\n")
            f.write("\n--- Statistiques globales ---\n")
            f.write(f"Moyenne : {moyenne:.2f}\n")
            f.write(f"Min : {minimum:.2f}\n")
            f.write(f"Max : {maximum:.2f}\n")
        print(f"✅ Rapport généré → {nom_fichier}")
    except Exception as e:
        print(f"❌ Erreur de génération du rapport : {e}")
