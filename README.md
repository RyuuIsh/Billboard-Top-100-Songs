# Billboard-Top-100-Songs
A Python script that scrapes Billboard's Hot 100 chart for a selected date and creates a Spotify playlist with the top songs from that year.

## Features
- Web Scraping – Extracts Billboard’s Top 100 songs using BeautifulSoup.
- Spotify Integration – Searches and adds songs to a private playlist automatically.
- Custom Date Selection – Users can choose any past date (YYYY-MM-DD) to generate a playlist.
- Secure API Authentication – Uses spotipy with OAuth for user authentication.

## Setup-Instructions
### Clone the Repository
```
git clone https://github.com/yourusername/Billboard-Spotify-Playlist.git
cd Billboard-Spotify-Playlist
```
### Install Dependencies
```
pip install -r requirements.txt
```
### Set Up Ennvironmental Variables
Create a .env file and add:
```
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
SPOTIPY_REDIRECT_URI=http://example.com
```
### Run the Script
```
python main.py
```
### Enter a Date
Type any date in YYYY-MM-DD format (e.g., 2000-07-15) to get the Billboard Hot 100 playlist.

## Tech-Stack
- Python – Core programming language
- BeautifulSoup – Web scraping
- Spotipy (Spotify API) – Playlist creation
- Requests – Fetching Billboard data

## Future-Enhancements
- Add artist names for better song matching.
- Allow public playlists for easy sharing.
- Implement Spotify login for multiple users.

🎧 Relive the best music from any year – right on your Spotify!


