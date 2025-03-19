import streamlit as st

def show():
    st.title("📺 Sélection de Chaînes YouTube Intéressantes")
    st.markdown("Découvrez ci-dessous une sélection de vidéos et chaînes YouTube directement accessibles.")

    # Liste de chaînes ou vidéos intéressantes
    videos = {
    "TSA Lecture - Adam Kashlak (playlist)": "https://www.youtube.com/embed/VSE8Ve-D3W4",
    "Time Series Analysis in Python | Time Series Forecasting | Data Science with Python | Edureka": "https://www.youtube.com/embed/e8Yw4alG16Q",
    "Pandas Time Series Analysis - codebasics": "https://www.youtube.com/embed/r0s4slGHwzE",
    "What is Time Series Analysis? - IBMTechnology": "https://www.youtube.com/embed/GE3JOFwTWVM",
    "Nonintrusive Load Monitoring (NILM) in a NUTSHELL - The Engineering Side": "https://www.youtube.com/embed/r03ar19NcN4",
    "Introduction to energy disaggregation with NILM - Data Science Milan": "https://www.youtube.com/embed/dj9qxgEwCAI"
}


    # Transformer les vidéos en liste de tuples (nom, url)
    video_items = list(videos.items())

    # Gestion des lignes (2 vidéos par ligne)
    for i in range(0, len(video_items), 2):
        cols = st.columns(2)  # Crée 2 colonnes

        for j in range(2):  # Pour chaque colonne
            if i + j < len(video_items):
                name, url = video_items[i + j]
                with cols[j]:  # Insérer la vidéo dans la colonne correspondante
                    st.markdown(f"#### {name}")
                    st.markdown(
                        f"""
                        <iframe width="80%" height="400" src="{url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                        """,
                        unsafe_allow_html=True
                    )
