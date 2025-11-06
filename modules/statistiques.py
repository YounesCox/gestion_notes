def afficher_tableau_bord_statistique(gestion_notes):
    if gestion_notes.df_notes.empty:
        print("📭 Aucune note disponible")
        return
    df = gestion_notes.df_notes
    print(f"\n📈 Moyenne: {df['Note'].mean():.2f}/20")
    print(f"📉 Minimum: {df['Note'].min():.2f}/20")
    print(f"🏆 Maximum: {df['Note'].max():.2f}/20")
