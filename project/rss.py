# categories.py
import streamlit as st
import feedparser
import pandas as pd
from datetime import datetime, timedelta
import pytz
from bs4 import BeautifulSoup
from utils import clean_html, parse_date

# Définition des catégories et mots-clés
CATEGORIES = {
    "Séries temporelles": [
        "time series", "forecasting", "temporal data", "time series analysis", "time series prediction", "time series modeling", "time series forecasting", "time series classification"
    ],
    "Méthodes avancées": [
        "ARIMA", "SARIMA", "LSTM time series", "Transformer time series", "Bayesian time series", "GAN time series", "time series clustering", "time series anomaly detection"
    ],
    "NILM (Non-Intrusive Load Monitoring)": [
        "NILM", "Non-Intrusive Load Monitoring", "load disaggregation", "energy monitoring", "smart meter", "appliance recognition", "energy disaggregation", "energy consumption", "energy monitoring", "energy efficiency"
    ],
    "Applications en entreprise": [
        "predictive maintenance", "demand forecasting", "anomaly detection", "energy efficiency", "fraud detection", "financial forecasting", "stock market prediction", "healthcare forecasting"
    ],
    "Modèles et algorithmes": [
        "Hidden Markov Models", "Gaussian Processes", "Reinforcement Learning", "Autoencoders", "Convolutional Neural Networks", "Random Forest", "Gradient Boosting", "XGBoost", "CatBoost"
    ]
}

# Références temporelles
DATE_REFERENCE = datetime(2025, 1, 15, tzinfo=pytz.UTC)
DATE_MIN = DATE_REFERENCE - timedelta(days=10 * 365)

# Chargement des flux RSS
@st.cache_data(ttl=43200)
def load_rss_urls():
    try:
        df = pd.read_csv("data/rss_urls.csv", header=None)
        return df[0].tolist()
    except Exception as e:
        st.error(f"Erreur lors du chargement du fichier CSV : {e}")
        return []

# Chargement de tous les articles depuis les flux
@st.cache_data(ttl=43200)
def fetch_all_rss_feeds(urls):
    all_articles = []
    for url in urls:
        all_articles.extend(fetch_rss_feed(url))
    return all_articles

# Récupération d'un flux unique
def fetch_rss_feed(url):
    try:
        feed = feedparser.parse(url)
        articles = []
        for entry in feed.entries:
            title = getattr(entry, 'title', 'Titre inconnu')
            description = getattr(entry, 'summary', 'Description non disponible')
            description_cleaned = clean_html(description)
            link = getattr(entry, 'link', '#')
            published_date = parse_date(getattr(entry, 'published', ''))
            if published_date:
                articles.append({
                    'title': title,
                    'description': description_cleaned,
                    'link': link,
                    'published': published_date
                })
        return articles
    except Exception as e:
        st.error(f"Erreur flux RSS {url} : {e}")
        return []

# Filtrage par mots-clés et gestion des dates
def filter_articles_by_keywords(articles, keywords):
    filtered_articles = []
    count_after_reference = 0
    now = datetime.now(pytz.UTC)  # Date actuelle en UTC
    for article in articles:
        content = (article['title'] + " " + (article['description'] or "")).lower()
        if any(keyword.lower() in content for keyword in keywords):
            # Inclure tous les articles pertinents dans la période DATE_MIN -> aujourd'hui
            if DATE_MIN <= article['published'] <= now:
                filtered_articles.append(article)
            # Compter les articles postérieurs à la date de référence
            if article['published'] > DATE_REFERENCE:
                count_after_reference += 1
    return filtered_articles, count_after_reference

# Affichage principal
def show():
    st.title("📚 Sélection d'articles par catégorie")
    st.markdown("Choisissez une thématique pour explorer les derniers articles pertinents issus de flux RSS spécialisés.")

    # Menu déroulant pour la catégorie
    selected_category = st.selectbox("📂 Choisissez une catégorie", list(CATEGORIES.keys()))

    # Chargement des flux RSS
    rss_urls = load_rss_urls()
    if not rss_urls:
        st.error("❌ Aucun flux RSS trouvé dans le fichier CSV.")
        return

    # Récupération des articles
    with st.spinner('🔄 Chargement des articles...'):
        all_articles = fetch_all_rss_feeds(rss_urls)

    # Filtrage selon les mots-clés
    keywords = CATEGORIES[selected_category]
    filtered_articles, count_after_reference = filter_articles_by_keywords(all_articles, keywords)

    # ✅ Tri dynamique
    st.markdown("---")
    sort_order = st.radio(
        "📊 Trier les articles par date :",
        ("📅 Du plus récent au plus ancien", "📅 Du plus ancien au plus récent"),
        horizontal=True
    )
    ascending = sort_order == "📅 Du plus ancien au plus récent"

    # Appliquer le tri selon le choix
    filtered_articles = sorted(filtered_articles, key=lambda x: x['published'], reverse=not ascending)

    # Résumé
    st.markdown("---")
    st.subheader(f"🔎 Résultats pour : {selected_category}")
    st.metric(label="📅 Articles récents (postérieurs au 15/01/2025)", value=count_after_reference)
    st.markdown("---")

    # Affichage des articles triés
    if filtered_articles:
        for article in filtered_articles:
            is_new = article['published'] > DATE_REFERENCE
            new_badge = "🆕" if is_new else ""

            with st.container():
                st.markdown(
                    f"""
                    <div style='border: 1px solid #ddd; padding: 15px; border-radius: 10px; background-color: #f9f9f9; margin-bottom: 10px;'>
                        <h4>{article['title']} {new_badge}</h4>
                        <p><strong>📅 Publié le :</strong> {article['published'].strftime('%d %B %Y')}</p>
                        <p>{article['description']}</p>
                        <a href="{article['link']}" target="_blank">🔗 Lire l'article complet</a>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    else:
        st.warning("⚠️ Aucun article trouvé pour cette catégorie et cette période.")
