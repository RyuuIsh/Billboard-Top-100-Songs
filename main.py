from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#Scrapping Billboard 100
date_str = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date_str)
soup =BeautifulSoup(response.text, "html.parser")
song_name_spans = soup.find_all(name="h3", class_="a-no-trucate")
song_names = [song.getText().strip() for song in song_name_spans]

Client_ID = "Your_Client_ID"
Client_Secret = "Your_client_server"
Redirect_URL = "http://example.com"

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=Redirect_URL,
        client_id= "Your_Client_ID",
        client_secret= "Your_client_server",
        show_dialog= True,
        cache_path= "token.txt", # Provide a token from Spotify in a new text file
        username="Your_Username"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#Searching spotify for songs by title
song_uris = []
year = date_str.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date_str} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

