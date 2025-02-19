from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Billboard Hot 100 Scraper
date_str = input("Which year do you want to travel to? Type the date in YYYY-MM-DD format: ")
billboard_url = f"https://www.billboard.com/charts/hot-100/{date_str}"
response = requests.get(billboard_url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract song titles
song_name_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_name_spans]

# Spotify Credentials from Environment Variables
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = "http://example.com"

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
    )
)

# Get User ID
user_id = sp.current_user()["id"]

# Searching Spotify for Songs
song_uris = []
year = date_str.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} not found on Spotify. Skipping...")

# Create a New Playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{date_str} Billboard 100", public=False)

# Add Songs to Playlist
if song_uris:
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
    print(f"Playlist '{date_str} Billboard 100' created successfully! ✅")
else:
    print("No songs found on Spotify. Playlist was not created.")
