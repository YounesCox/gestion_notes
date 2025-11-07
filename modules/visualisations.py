import matplotlib.pyplot as plt

def afficher_graphique_notes(gestion_notes):
    """Affiche un graphique en barres des notes."""
    if gestion_notes.df_notes.empty:
        print("📭 Aucune donnée à afficher.")
        return
    
    df = gestion_notes.df_notes.sort_values(by='Note', ascending=False)
    plt.figure(figsize=(8, 4))
    plt.bar(df['Nom'], df['Note'])
    plt.title("📊 Répartition des notes par élève")
    plt.xlabel("Nom")
    plt.ylabel("Note (/20)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def afficher_histogramme(gestion_notes):
    """Affiche un histogramme des notes."""
    if gestion_notes.df_notes.empty:
        print("📭 Aucune donnée à afficher.")
        return
    
    plt.figure(figsize=(6, 4))
    plt.hist(gestion_notes.df_notes['Note'], bins=5, edgecolor='black')
    plt.title("📈 Distribution des notes")
    plt.xlabel("Note (/20)")
    plt.ylabel("Nombre d'élèves")
    plt.tight_layout()
    plt.show()
