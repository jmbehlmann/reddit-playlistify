import praw, os, requests, json
from dotenv import load_dotenv
from praw.models import MoreComments

load_dotenv()

playlist_id = "5nt6uJH4N89CUMSOUnse3m"

access_token = "BQC0SaQhAdhnMJIuCwwZTDwcKrxwDL1SKFsQjll1fyQU52LextEaOok3SWVhkwPczoNvrvX5sIMYSCOGzbi_kVcUeuJLBioUellhcsDzjyTsCCxrqrOGMJhTZvnLWhT52HLP5BV2Pl-1YR9jVgJYiISs_xMYnGYWMUt8mYZE6uKfVRhDEeSApA9Pibw7FTLsXSKQ4_BtSAOXS5VsgHxk9bdja9nwcFZzTNPrjWl5M3JlZnbtp7ppt8RKqg"

albums = ['Slint Spiderland', 'Lingua Ignota Caligula', 'A promise xiu xiu', 'El-P’s I’ll Sleep When You’re Dead', 'Yo La Tengo I Can Heart the Heart Beating as One', 'Red King Crimson', 'Koyaanisqatsi by Philip Glass', 'Talk Talk Laughing Stock', 'The Microphones The Glow, Pt 2', 'my bloody valentine loveless', 'Glenn Branca The Ascension', 'Natural Snow Buildings The Dance of the Moon and the Sun', 'nine inch nails the fragile', 'Death Grips The Money Store', 'Radiohead Kid A', 'Low Secret Name', 'To Be Cruel Khantae', 'Laibach sketches of the red district', 'manic street preachers the holy bible', 'Lift Your Skinny Dick Like Antenna To Heaven', 'Pink Floyd Wish You Were Here', 'SPELLLING The Turning Wheel']

album_id = "2NnkLRaeX33d1Mn8ZLgTo8"


url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'

# Define the headers with the access token
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Define the data payload with the album ID
data = {
    'uris': [f'spotify:album:{album_id}']
}

# Make the POST request to add the album to the playlist
response = requests.post(url, headers=headers, json=data)

# Check if the request was successful (status code 200)
if response.status_code == 201:
    print('Album added to playlist successfully!')
else:
    print('Failed to add album to playlist:', response.text)
