from app import app
from flask import render_template
from .request import get_sources, get_articles

@app.route("/")
def index():

    general = get_sources('general')
    business_source_data = get_sources('business')
    sports_source_data = get_sources('sports')
    entertainment_source_data = get_sources('entertainment')
    title = "The Times"
    return render_template("index.html", title = title, business_news_sources = business_source_data, sports_news_sources = sports_source_data, general_news_sources = general, entertainment_news_sources = entertainment_source_data)