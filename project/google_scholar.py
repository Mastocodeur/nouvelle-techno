import streamlit as st
from scholarly import scholarly

def get_articles(query, max_results=20):
    """Recherche des articles via Google Scholar"""
    search_query = scholarly.search_pubs(query)
    results = []
    for i in range(max_results):
        try:
            article = next(search_query)
            results.append({
                "title": article['bib']['title'],
                "author": article['bib'].get('author', 'Inconnu'),
                "year": article['bib'].get('pub_year', 'N/A'),
                "link": article.get('pub_url', 'Non disponible')
            })
        except StopIteration:
            break
    return results

def show():
    st.title("🔎 Recherche Google Scholar")

    # ✅ Encadré explicatif pour aider à formuler la requête
    st.markdown(
    """
    <div style='border: 2px solid #0077B5; padding: 15px; border-radius: 10px; background-color: #f0f8ff; margin-bottom: 20px;'>
        <h4>🧠 Comment bien formuler une requête Google Scholar :</h4>
        <ul>
            <li><strong>since:2020</strong> : Limite aux articles depuis 2020.</li>
            <li><strong>intitle:"deep learning"</strong> : Cherche "deep learning" uniquement dans les titres.</li>
            <li><strong>author:"Goodfellow"</strong> : Limite aux articles d'un auteur donné.</li>
            <li><strong>filetype:pdf</strong> : Limite aux fichiers PDF.</li>
        </ul>
        <h5>💡 Exemple de requête combinée :</h5>
        <p><code>time series forecasting intitle:"deep learning" since:2021 filetype:pdf author:"Goodfellow"</code></p>
        <p>👉 Cette requête cherchera des articles récents sur la prévision de séries temporelles avec "deep learning" dans le titre, écrits par "Goodfellow", et disponibles en PDF.</p>
    </div>
    """,
    unsafe_allow_html=True
)


    # Champ de recherche
    query = st.text_input("💬 Tapez votre requête Google Scholar ici")

    if query:
        with st.spinner("🔍 Recherche en cours..."):
            articles = get_articles(query, max_results=20)  # Charger plus pour trier ensuite

        # ✅ Trier les articles par année décroissante
        articles_with_valid_year = [a for a in articles if a['year'].isdigit()]

        # ✅ Trier par année décroissante
        articles_sorted = sorted(articles_with_valid_year, key=lambda x: int(x['year']), reverse=True)

        # Limiter aux 5 plus récents
        articles_sorted = articles_sorted[:5]

        if articles_sorted:
            for art in articles_sorted:
                st.markdown(
                    f"""
                    <div style='border: 1px solid #ddd; padding: 15px; border-radius: 10px; margin-bottom: 10px; background-color: #f9f9f9;'>
                        <h4>{art['title']}</h4>
                        <p><strong>Auteurs :</strong> {art['author']}</p>
                        <p><strong>Année :</strong> {art['year']}</p>
                        <p><a href="{art['link']}" target="_blank">🔗 Lien vers l'article</a></p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.warning("⚠️ Aucun article récent trouvé pour cette requête.")
