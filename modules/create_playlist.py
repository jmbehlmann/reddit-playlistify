import praw, os, requests, json
from dotenv import load_dotenv
from praw.models import MoreComments
load_dotenv()

thread = ""


title = ""

# get access token from spotify_auth.py

access_token = ""

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
