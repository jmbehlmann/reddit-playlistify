import praw, os, requests, json
from dotenv import load_dotenv
from praw.models import MoreComments
load_dotenv()

thread = "https://www.reddit.com/r/swans/comments/1c2n4y1/day_4_what_are_swans_fans_favorite_albums_outside/"


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
