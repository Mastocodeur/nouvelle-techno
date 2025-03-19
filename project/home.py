import streamlit as st
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, "images", "outils.jpg")

def show():
    st.title("Accueil")
    # Encadré de présentation
    with st.container():
        st.markdown(
            """
            <div style='border: 2px solid #4CAF50; padding: 15px; border-radius: 10px; background-color: #f9f9f9;'>
                <h3>Outil de Veille Technologique</h3>
                <p>Cette application vous permet de suivre en temps réel plusieurs flux RSS catégorisés, de visualiser
                un certain nombre de vidéos YouTube, de consulter des profils LinkedIn et de rechercher des articles
                sur Google Scholar sur le sujet des Séries temporelles, NILM et Techniques d’analyse.</p> 
                <p>L'objectif est de proposer une interface simple et ergonomique. </p>
                <p>Elle permet de consulter les dernières actualités, trier par thématique et accéder rapidement aux contenus les plus pertinents.</p> </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Affichage de l'image
    st.image(
        image_path,  
        #caption="Dashboard RSS - Suivi en temps réel",
        use_container_width=True
    )

    st.markdown("---")

    # Titre liens utiles
    st.header("📚 Liens Utiles")

    # Liste des liens utiles
    useful_links = [
        {"title": "📂 Source du projet sur GitHub", "url": "https://github.com/Mastocodeur/nouvelle-techno/tree/main"},
        {"title": "📖 Documentation sur les flux RSS", "url": "https://fr.wikipedia.org/wiki/RSS"},
        {"title": "📬 Contact / Signaler un problème", "url": "mailto:remy.gasmi@gmail.com"},
    ]

    # Grille en 2 colonnes
    cols = st.columns(2) 

    # Affichage des cartes compactes
    for i, link in enumerate(useful_links):
        with cols[i % 2]:  # Répartition dans les colonnes
            st.markdown(
                f"""
                <a href="{link['url']}" target="_blank" style="text-decoration: none;">
                    <div style='
                        border: 1px solid #0077B5;
                        padding: 10px;
                        border-radius: 8px;
                        margin-bottom: 10px;
                        background-color: #f0f8ff;
                        text-align: center;
                        font-size: 14px;
                        line-height: 1.4;
                        min-height: 60px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    '>
                        <strong>{link['title']}</strong>
                    </div>
                </a>
                """,
                unsafe_allow_html=True
            )
