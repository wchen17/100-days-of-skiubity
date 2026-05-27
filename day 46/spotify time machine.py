# ============================================================
#  DAY 46: Web Scraping Project
#  PROJECT: Spotify Time Machine (Billboard → Playlist)
# ============================================================
#
#  SKILLS TODAY:
#    - Scrape Billboard Hot 100 for a given date
#    - Spotipy (Spotify API wrapper): pip install spotipy
#    - OAuth authentication with Spotipy
#    - Creating a private Spotify playlist
#    - Searching for tracks by name + year
#
#  pip install requests beautifulsoup4 spotipy
#
# ============================================================

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

date = input("Which year do you want to travel to? Type the date in YYYY-MM-DD: ")
URL  = f"https://www.billboard.com/charts/hot-100/{date}"

# --------------------------------------------------
#  TODO 1: Scrape the Billboard Hot 100 for that date
# --------------------------------------------------
# Fetch the URL and parse with BeautifulSoup
# Find the song title elements (inspect the page to find the right selector)
# Hint: look for <li> with class containing "chart-results-list" or
#       <h3> with id="title-of-a-story"

response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

# song_titles_spans = soup.select("li ul li h3")  ← adjust selector as needed
# songs = [song.get_text().strip() for song in song_titles_spans]
songs = ["Song A", "Song B", "Song C"]   # placeholder until you scrape

print(f"Top songs from {date}:")
for i, song in enumerate(songs[:10], 1):
    print(f"  {i}. {song}")


# --------------------------------------------------
#  TODO 2: Authenticate with Spotify
# --------------------------------------------------
# Set up a Spotify app at developer.spotify.com
# Get Client ID, Client Secret, and set Redirect URI to http://example.com
# Add to .env: SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI", "http://example.com"),
        scope="playlist-modify-private",
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]


# --------------------------------------------------
#  TODO 3: Search for each song on Spotify
# --------------------------------------------------
# For each song name:
#   result = sp.search(q=f"track:{song} year:{date[:4]}", type="track")
#   If result found → get the URI from result["tracks"]["items"][0]["uri"]
#   Else → print that song wasn't found

song_uris = []
year = date.split("-")[0]

for song in songs:
    # result = sp.search(q=f"track:{song} year:{year}", type="track")
    # try:
    #     uri = result["tracks"]["items"][0]["uri"]
    #     song_uris.append(uri)
    # except IndexError:
    #     print(f"{song} not found on Spotify.")
    pass


# --------------------------------------------------
#  TODO 4: Create a private playlist and add the tracks
# --------------------------------------------------
# playlist = sp.user_playlist_create(user_id, f"{date} Billboard 100", public=False)
# sp.playlist_add_items(playlist["id"], song_uris)
# print(f"Playlist created: {playlist['external_urls']['spotify']}")
