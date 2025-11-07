import streamlit as st
import pandas as pd
from models.gestion_notes import GestionNotes
from modules.statistiques import afficher_tableau_bord_statistique
from modules.visualisations import afficher_graphique_notes, afficher_histogramme
from modules.decision import afficher_dashboard_decisionnel
from modules.exportation import exporter_csv, generer_rapport_texte

# Initialisation
gestion_notes = GestionNotes()

st.set_page_config(page_title="Système de Gestion des Notes", page_icon="🎓", layout="centered")

st.title("🎓 Système de Gestion des Notes")
st.write("Bienvenue dans votre interface web de gestion académique.")

# Barre de navigation
menu = st.sidebar.selectbox(
    "Menu",
    ["Accueil", "Gestion des notes", "Statistiques", "Graphiques", "Décision", "Exportation"]
)

# Gestion des notes
if menu == "Gestion des notes":
    st.header("📝 Gestion des notes")
    if st.button("Afficher toutes les notes"):
        st.dataframe(gestion_notes.df_notes)
    
    with st.expander("➕ Ajouter une nouvelle note"):
        nom = st.text_input("Nom de l’étudiant")
        note = st.number_input("Note (/20)", min_value=0.0, max_value=20.0, step=0.5)
        if st.button("Enregistrer la note"):
            nouvelle_ligne = pd.DataFrame([{"Nom": nom, "Note": note}])
            gestion_notes.df_notes = pd.concat([gestion_notes.df_notes, nouvelle_ligne], ignore_index=True)
            gestion_notes.sauvegarder_notes()
            st.success(f"Note ajoutée pour {nom}")

# Statistiques
elif menu == "Statistiques":
    st.header("📊 Tableau de bord statistique")
    if gestion_notes.df_notes.empty:
        st.warning("Aucune donnée disponible.")
    else:
        df = gestion_notes.df_notes
        st.metric("Moyenne", f"{df['Note'].mean():.2f}/20")
        st.metric("Maximum", f"{df['Note'].max():.2f}/20")
        st.metric("Minimum", f"{df['Note'].min():.2f}/20")

# Graphiques
elif menu == "Graphiques":
    st.header("📈 Visualisation des notes")
    if gestion_notes.df_notes.empty:
        st.warning("Aucune donnée disponible.")
    else:
        st.subheader("Graphique des notes par élève")
        st.bar_chart(gestion_notes.df_notes.set_index("Nom")["Note"])
        st.subheader("Histogramme des notes")
        st.pyplot(afficher_histogramme(gestion_notes))

# Décision
elif menu == "Décision":
    st.header("💡 Dashboard décisionnel")
    df = gestion_notes.df_notes
    if not df.empty:
        moyenne = df['Note'].mean()
        if moyenne >= 16:
            st.success("🌟 Excellent niveau général")
        elif moyenne >= 12:
            st.info("✅ Niveau satisfaisant")
        elif moyenne >= 10:
            st.warning("⚠️ Niveau moyen")
        else:
            st.error("❌ Niveau insuffisant")
    else:
        st.warning("Aucune donnée à analyser")

# Exportation
elif menu == "Exportation":
    st.header("💾 Exportation des données")
    if st.button("Exporter en CSV"):
        exporter_csv(gestion_notes)
    if st.button("Générer rapport texte"):
        generer_rapport_texte(gestion_notes)

# Accueil
else:
    st.header("🏠 Accueil")
    st.write("Utilisez le menu de gauche pour naviguer entre les différentes fonctionnalités.")
