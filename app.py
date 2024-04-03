from flask import Flask
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)

@app.route('/')
def billboard_charts():
    chart_date = "1990-01-01" #input("Bitte bitte gib ein Datum ein, für welches du die Charts abrufen möchtest (Format: YYYY-MM-DD): ")
    # Todo check input
    # Get website
    response = requests.get(f"https://www.billboard.com/charts/hot-100/{chart_date}")
    # Parse website
    soup = BeautifulSoup(response.text, 'html.parser')
    # Select tags with song titles
    song_names_spans = soup.select("li ul li h3")
    # extract song title
    song_names = [song.getText().strip() for song in song_names_spans]
    return song_names


# @app.route('/')
# def hello_world():
#     return 'Hello from Koyeb'


if __name__ == "__main__":
    app.run()
