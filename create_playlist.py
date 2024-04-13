import praw, os, requests, json
from dotenv import load_dotenv
from praw.models import MoreComments
load_dotenv()



albums = ['Slint Spiderland', 'Lingua Ignota Caligula', 'A promise xiu xiu', 'El-P’s I’ll Sleep When You’re Dead', 'Yo La Tengo I Can Heart the Heart Beating as One', 'Red King Crimson', 'Koyaanisqatsi by Philip Glass', 'Talk Talk Laughing Stock', 'The Microphones The Glow, Pt 2', 'my bloody valentine loveless', 'Glenn Branca The Ascension', 'Natural Snow Buildings The Dance of the Moon and the Sun', 'nine inch nails the fragile', 'Death Grips The Money Store', 'Radiohead Kid A', 'Low Secret Name', 'To Be Cruel Khantae', 'Laibach sketches of the red district', 'manic street preachers the holy bible', 'Lift Your Skinny Dick Like Antenna To Heaven', 'Pink Floyd Wish You Were Here', 'SPELLLING The Turning Wheel']

title = "(DAY 4) What are swans fans favorite albums outside of swans?"


# get token
url = "https://accounts.spotify.com/api/token"
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
    'grant_type': 'client_credentials',
    'client_id': os.environ.get('SPOTIFY_CLIENT_ID'),
    'client_secret': os.environ.get('SPOTIFY_CLIENT_SECRET')
}


# response = requests.post(url, data=data)

# if response.status_code == 200:
#     # Extract the access token from the response JSON
#     access_token = response.json()['access_token']
#     print("Access token:", access_token)
# else:
#     # Print an error message if the request failed
#     print("Failed to get access token:", response.text)

access_token = "BQDCdJ3F6RSDuLsKv15MyIUej4RcSEc_it4Ka-LPPCY2CGjeTy9wvkaIi6D5d9bXk5B7sWiPvMI2fUc8o9dT0l6L1hyXXVuUiI0f8kZBwwnXZyhVTv2H9QzrxVxaAbQi3m7X1ZMadT1CxOiA_mXONPgYFuhJrY9yaQFKm6unnWaeJM6ecHC18HotTrAGRus"

# get user id

url = "https://api.spotify.com/v1/me"


response = requests.get(url, headers={'Authorization': f'Bearer {access_token}'})

print(response.json())
