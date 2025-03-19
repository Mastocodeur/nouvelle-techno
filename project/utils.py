from bs4 import BeautifulSoup
from datetime import datetime
import pytz

def clean_html(raw_html):
    """Nettoie le HTML pour extraire uniquement du texte brut."""
    soup = BeautifulSoup(raw_html, "html.parser")
    return soup.get_text()

def parse_date(date_str):
    """Convertit une chaîne de date en objet datetime avec gestion de plusieurs formats."""
    date_formats = [
        "%a, %d %b %Y %H:%M:%S %z",
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%d %H:%M:%S",
    ]
    for fmt in date_formats:
        try:
            dt = datetime.strptime(date_str, fmt)
            return dt.replace(tzinfo=pytz.UTC) if dt.tzinfo is None else dt
        except ValueError:
            continue
    return None
