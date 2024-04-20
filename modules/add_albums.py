import praw, os, requests, json
from dotenv import load_dotenv
from praw.models import MoreComments

load_dotenv()

playlist_id = ""

access_token = ""

track_ids = []

formatted_track_ids = []

for track_id in track_ids:
    formatted_track_ids.append(f'spotify:track:{track_id}')

print(formatted_track_ids)

album_id = "2NnkLRaeX33d1Mn8ZLgTo8"


url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'

# Define the headers with the access token
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Define the data payload with the album ID
data = {
    'uris': formatted_track_ids
}

# Make the POST request to add the album to the playlist
response = requests.post(url, headers=headers, json=data)

# Check if the request was successful (status code 200)
# if response.status_code == 201:
#     print('Album added to playlist successfully!')
# else:
#     print('Failed to add album to playlist:', response.text)
