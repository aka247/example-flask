# commit via sourcetree
# projekteinstellungen https://app.koyeb.com/apps/new/configure-service?service_type=web&type=git&repository=github.com%2Faka247%2Fkoyeb


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

#
# from bs4 import BeautifulSoup
# import requests
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
#
# # Scraping Billboard 100
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
# soup = BeautifulSoup(response.text, 'html.parser')
# song_names_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_names_spans]
#
# # Spotify Authentication
# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="http://example.com",
#         client_id=YOUR
# CLIENT
# ID,
# client_secret = YOUR
# CLIENT
# SECRET,
# show_dialog = True,
# cache_path = "token.txt"
# )
# )
# user_id = sp.current_user()["id"]
# print(user_id)
#
# # Searching Spotify for songs by title
# song_uris = []
# year = date.split("-")[0]
# for song in song_names:
#     result = sp.search(q=f"track:{song} year:{year}", type="track")
#     print(result)
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(uri)
#     except IndexError:
#         print(f"{song} doesn't exist in Spotify. Skipped.")
#
# # Creating a new private playlist in Spotify
# playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)
#
# # Adding songs found into the new playlist
# sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
#
