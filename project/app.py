# app.py
import streamlit as st
from streamlit_option_menu import option_menu
import home
import rss
import youtube
import google_scholar  
# import gmail  # Commenté si non utilisé
import linkedin
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
from datetime import datetime, timedelta
import pytz
from utils import clean_html, parse_date


# Configuration générale de la page
st.set_page_config(page_title="Dashboard RSS", layout="wide")


def main():
    # Barre de navigation horizontale avec icônes
    selected_page = option_menu(
        menu_title=None,  # Pas de titre
        options=["Accueil", "Flux RSS", "Youtube", "LinkedIn", "Google Scholar"],  # Pages
        icons=["house", "rss", "youtube", "linkedin", "google"],  # Icônes bootstrap
        menu_icon="cast",  # Icône du menu (si tu veux l'activer)
        default_index=0,  # Page par défaut
        orientation="horizontal",  # Horizontal navbar
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "18px"},
            "nav-link": {
                "font-size": "18px",
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#02ab21", "color": "white"},
        },
    )

    # Dictionnaire des pages reliées à leur fonction
    pages = {
        "Accueil": home.show,
        "Flux RSS": rss.show,
        "Youtube": youtube.show,
        "LinkedIn": linkedin.show,
        "Google Scholar": google_scholar.show,
    }

    # Appel de la fonction correspondant à la page sélectionnée
    pages[selected_page]()


if __name__ == "__main__":
    main()
