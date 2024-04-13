import praw, os, requests, json
from dotenv import load_dotenv
from praw.models import MoreComments
load_dotenv()

thread = "https://www.reddit.com/r/swans/comments/1c2n4y1/day_4_what_are_swans_fans_favorite_albums_outside/"

albums = ['Slint Spiderland', 'Lingua Ignota Caligula', 'A promise xiu xiu', 'El-P’s I’ll Sleep When You’re Dead', 'Yo La Tengo I Can Heart the Heart Beating as One', 'Red King Crimson', 'Koyaanisqatsi by Philip Glass', 'Talk Talk Laughing Stock', 'The Microphones The Glow, Pt 2', 'my bloody valentine loveless', 'Glenn Branca The Ascension', 'Natural Snow Buildings The Dance of the Moon and the Sun', 'nine inch nails the fragile', 'Death Grips The Money Store', 'Radiohead Kid A', 'Low Secret Name', 'To Be Cruel Khantae', 'Laibach sketches of the red district', 'manic street preachers the holy bible', 'Lift Your Skinny Dick Like Antenna To Heaven', 'Pink Floyd Wish You Were Here', 'SPELLLING The Turning Wheel']

title = "(DAY 4) What are swans fans favorite albums outside of swans?"

# get access token from spotify_auth.py

access_token = "BQC0SaQhAdhnMJIuCwwZTDwcKrxwDL1SKFsQjll1fyQU52LextEaOok3SWVhkwPczoNvrvX5sIMYSCOGzbi_kVcUeuJLBioUellhcsDzjyTsCCxrqrOGMJhTZvnLWhT52HLP5BV2Pl-1YR9jVgJYiISs_xMYnGYWMUt8mYZE6uKfVRhDEeSApA9Pibw7FTLsXSKQ4_BtSAOXS5VsgHxk9bdja9nwcFZzTNPrjWl5M3JlZnbtp7ppt8RKqg"

# get user id

url = "https://api.spotify.com/v1/me"


response = requests.get(url, headers={'Authorization': f'Bearer {access_token}'})

user_data = response.json()
user_id = user_data['id']
print(user_id)


url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}
data = {
    "name": f"{title}",
    "description": f"From reddit thread {thread}",
    "public": False
}

response = requests.post(url, headers=headers, json=data)

playlist_data = response.json()
playlist_id = playlist_data['id']
print(playlist_id)
