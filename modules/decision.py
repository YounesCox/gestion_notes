def afficher_dashboard_decisionnel(gestion_notes):
    """Propose une interprétation automatique des résultats."""
    if gestion_notes.df_notes.empty:
        print("📭 Aucune donnée disponible pour l’analyse.")
        return
    
    moyenne = gestion_notes.df_notes['Note'].mean()
    if moyenne >= 16:
        decision = "🌟 Excellent niveau général."
    elif moyenne >= 12:
        decision = "✅ Niveau satisfaisant."
    elif moyenne >= 10:
        decision = "⚠️ Niveau moyen, des efforts sont nécessaires."
    else:
        decision = "❌ Niveau insuffisant, un plan de rattrapage est recommandé."
    
    print("\n📊 DASHBOARD DÉCISIONNEL")
    print("-" * 40)
    print(f"Moyenne générale : {moyenne:.2f}/20")
    print(f"Décision : {decision}")
    print("-" * 40)
