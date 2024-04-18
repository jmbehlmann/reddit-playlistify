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

code = "AQB6EieesaqduWoT66lH9vWNXPA8jwzk4DPRFP4FUCHIL0vZnCYMPUN3inObDj7Vz2k3ACCNNajvDn-dBX85r5pOzPXnmCxRDzePRKHJTCNLkI-GoE1JK2h91QSm3CMKCRxfLAcymkZuYttDWPuFrh1ucrpSwbXfZICL1L432amDOjV-_oe-4N3p4bDHUjqtT6XIjhdYJGFv4gigD-MRGbLn8O24nrD6ZXNBbFK6HNj0O6ByDIW_HY9m0hsJIgL0uTjl_4la"


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
