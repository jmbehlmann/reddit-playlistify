import requests, os
from urllib.parse import urlencode
from dotenv import load_dotenv
import base64
import webbrowser

load_dotenv()

client_id = os.environ.get('SPOTIFY_CLIENT_ID')
client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')

# auth_headers = {
#     "client_id": client_id,
#     "response_type": "code",
#     "redirect_uri": "http://localhost:8080/callback",
#     "scope": "user-library-read playlist-modify-private playlist-modify-public"
# }

# webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

# code will be in url of redirect window

code = "AQAKyxO5FkqhpOA-CnT7s-eLU-MuBeu8-tpzbIw1IviBDKslqUabX6fUl2-7SbZvlOQFZ_D1KeTKSp-pq98QE1a_b-No0Svnnj7OnBh70W0R2j6s8e0cZFD1ZZHDKulRcDKntMIMONJUUVmweZ4DHqAPfmb6JcNFnikmdZ3WoDpw-JpDv8QeItxMKCZcF0P9UH6968AdYVCRn217aWc9KFXJ11aLS3g9apdhKCHxp6jmtk2bBhsA-dMvLXERxJp_2mqP8DjE"


encoded_credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")

token_headers = {
    "Authorization": "Basic " + encoded_credentials,
    "Content-Type": "application/x-www-form-urlencoded"
}

token_data = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": "http://localhost:8080/callback"
}

r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)

token = r.json()["access_token"]

print(token)
