import streamlit as st
import os
import base64

def get_base64_image(image_path):
    """Convertit une image locale en Base64 pour l'afficher dans un lien"""
    with open(image_path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    return f"data:image/png;base64,{encoded}"

# Définir le chemin de l'image
IMAGE_PATH = os.path.join("images", "linkedin.png")
link_url = "https://www.linkedin.com"

# Liste des liens définis en dur dans le code
LINKEDIN_LINKS = [
    {"title": "Profil de Benjamin Tardy", "url": "https://www.linkedin.com/in/benjamin-tardy/"},
    {"title": "Profil de Gael Penessot", "url": "https://www.linkedin.com/in/gael-penessot/"},
    {"title": "Profil de Marwa Dhifallah", "url": "https://www.linkedin.com/in/marwa-dhifallah/"},
    {"title": "Profil de Sane Lebrun", "url": "https://www.linkedin.com/in/sanelebrun"},
    {"title": "Time Series Analysis, Forecasting, and Statistics", "url": "https://www.linkedin.com/groups/8538248/"},
    {"title": "Time Series Analysis and Forecasting Society", "url": "https://www.linkedin.com/groups/9219094/"},
    {"title": "Autobox User Group - Forecasting & Time Series Analysis, ARIMA, Outliers, Transfer Function & more!", "url": "https://www.linkedin.com/groups/2511642/"},
    {"title": "Python for Time Series Analysis", "url": "https://www.linkedin.com/groups/14250390/"},
]

def show():
    st.title("🔗 Liens utiles - LinkedIn")

    # Affichage de l'image LinkedIn cliquable
    if os.path.exists(IMAGE_PATH):
        base64_img = get_base64_image(IMAGE_PATH)
        st.markdown(
            f'<a href="{link_url}" target="_blank">'
            f'<img src="{base64_img}" width="150" style="margin-bottom: 20px;"></a>',
            unsafe_allow_html=True
        )
    else:
        st.warning(f"⚠️ Image LinkedIn non trouvée à : {IMAGE_PATH}")

    st.markdown("Voici une sélection de comptes LinkedIn qui proposent des newsletter et des groupes LinkedIn relatifs à notre sujet de veille :")

    # Barre de recherche
    search = st.text_input("🔎 Rechercher un profil LinkedIn")
    filtered_links = [link for link in LINKEDIN_LINKS if search.lower() in link['title'].lower()]

    # Affichage en colonnes (GRID)
    cols = st.columns(2)  

    for idx, link in enumerate(filtered_links):
        with cols[idx % len(cols)]:  # Répartition automatique dans les colonnes
            st.markdown(
                f"""
                <div style='border: 1px solid #ddd; padding: 15px; border-radius: 10px; margin-bottom: 20px; background-color: #f9f9f9; text-align: center;'>
                    <h4 style='margin-bottom: 15px;'>{link['title']}</h4>
                    <a href="{link['url']}" target="_blank" style="text-decoration: none;">
                        <button style='background-color: #0077B5; color: white; padding: 10px 20px; border: none; border-radius: 5px; font-size: 16px;'>Voir sur LinkedIn</button>
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )
