import os
import spotipy
import requests
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv, dotenv_values

load_dotenv()

CL_ID = os.getenv("CL_ID")
CL_SD = os.getenv("CL_SD")
URL = "https://www.billboard.com/charts/hot-100"

date = input("what year you would like to travel to? (in YYY-MM-DD format)\n")

response = requests.get(url=f"{URL}/{date}")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
# titles = soup.find_all(name="h3",id="title-of-a-story",class_="c-title") wanted to test find all before select
songs = soup.select(selector="li ul li h3")
songs_list = [song.getText().strip() for song in songs]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CL_ID,
        client_secret=CL_SD,
        show_dialog=True,
        cache_path="web/Spotify Playlist/token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(
    user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
