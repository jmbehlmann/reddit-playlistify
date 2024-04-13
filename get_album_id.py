import praw, os, requests, json
from dotenv import load_dotenv
from praw.models import MoreComments

load_dotenv()

access_token = "BQC0SaQhAdhnMJIuCwwZTDwcKrxwDL1SKFsQjll1fyQU52LextEaOok3SWVhkwPczoNvrvX5sIMYSCOGzbi_kVcUeuJLBioUellhcsDzjyTsCCxrqrOGMJhTZvnLWhT52HLP5BV2Pl-1YR9jVgJYiISs_xMYnGYWMUt8mYZE6uKfVRhDEeSApA9Pibw7FTLsXSKQ4_BtSAOXS5VsgHxk9bdja9nwcFZzTNPrjWl5M3JlZnbtp7ppt8RKqg"

albums = ['Slint Spiderland', 'Lingua Ignota Caligula', 'A promise xiu xiu', 'El-P’s I’ll Sleep When You’re Dead', 'Yo La Tengo I Can Heart the Heart Beating as One', 'Red King Crimson', 'Koyaanisqatsi by Philip Glass', 'Talk Talk Laughing Stock', 'The Microphones The Glow, Pt 2', 'my bloody valentine loveless', 'Glenn Branca The Ascension', 'Natural Snow Buildings The Dance of the Moon and the Sun', 'nine inch nails the fragile', 'Death Grips The Money Store', 'Radiohead Kid A', 'Low Secret Name', 'To Be Cruel Khantae', 'Laibach sketches of the red district', 'manic street preachers the holy bible', 'Lift Your Skinny Dick Like Antenna To Heaven', 'Pink Floyd Wish You Were Here', 'SPELLLING The Turning Wheel']

# get album id

# Define the base URL for the Spotify API
url = 'https://api.spotify.com/v1/search'


# album = "Rubber Soul"
# artist = "Beatles"
# Define the search query
album = albums[0]
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
    print(f"album id for {album} is {album_id}")
    print(album_details)
else:
    # Print an error message if the request failed
    print("Failed to search for album:", response.text)


