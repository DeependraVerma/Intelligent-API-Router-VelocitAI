import requests

API_KEY = "your_newsapi_key"

def get_news(topic):
    """Fetches news using NewsAPI."""
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={API_KEY}"
    response = requests.get(url).json()
    articles = response["articles"][:3]
    return " | ".join([article["title"] for article in articles])
