import requests, os
from urllib.parse import urlencode
from dotenv import load_dotenv
import base64
import webbrowser

load_dotenv()

client_id = os.environ.get('SPOTIFY_CLIENT_ID')
client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')

auth_headers = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": "http://localhost:8080/callback",
    "scope": "user-library-read playlist-modify-private playlist-modify-public"
}

webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

# code will be in url of redirect window
