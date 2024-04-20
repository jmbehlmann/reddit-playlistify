import praw, os, requests, json
from dotenv import load_dotenv
from praw.models import MoreComments

load_dotenv()

access_token = "BQCb7nd_mxOmxxSJZGoSI_LP9vbvFomCAge5OzgPVSMjmEK4KXB7VKm1RRrHsoYAoCiXrXDjqhaGGPcyywemBeV2tfGjwFT7slwgGOURiLMmD9x4Fr-O0IrxDdgE2b-0inKjo1YfEKiknkXfUDwdFc8QaELuDYvFrOM3oTWsyy3NyOyb92NnbBSTIS16QowKTfjHr-0V58eRnLuiU8VirZTyztpPWqyrWiFuj-2nOzHyU00UL-dyNRdvCQ"

albums = ['Slint Spiderland', 'Lingua Ignota Caligula', 'A promise xiu xiu', 'El-P’s I’ll Sleep When You’re Dead', 'Yo La Tengo I Can Heart the Heart Beating as One', 'Red King Crimson', 'Koyaanisqatsi by Philip Glass', 'Talk Talk Laughing Stock', 'The Microphones The Glow, Pt 2', 'my bloody valentine loveless', 'Glenn Branca The Ascension', 'Natural Snow Buildings The Dance of the Moon and the Sun', 'nine inch nails the fragile', 'Death Grips The Money Store', 'Radiohead Kid A', 'Low Secret Name', 'To Be Cruel Khantae', 'Laibach sketches of the red district', 'manic street preachers the holy bible', 'Lift Your Skinny Dick Like Antenna To Heaven', 'Pink Floyd Wish You Were Here', 'SPELLLING The Turning Wheel']

# get album id

# Define the base URL for the Spotify API
url = 'https://api.spotify.com/v1/search'

album_ids = []

for album in albums:

    # Define the search query
    query = album

    # Define the parameters for the GET request
    params = {
        'q': query,
        'type': 'album',
        'limit': 1  # Limit the number of results to 1 (optional)
    }

    # Make the GET request with the access token
    response = requests.get(url, params=params, headers={'Authorization': f'Bearer {access_token}'})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the album details from the response JSON
        album_details = response.json()['albums']['items'][0]
        album_id = album_details['id']
        print(f"the album id for {album} is {album_id}")
        album_ids.append(album_id)
    else:
        # Print an error message if the request failed
        print("Failed to search for album:", response.text)

print(album_ids)
