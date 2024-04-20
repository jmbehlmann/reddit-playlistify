import praw, os, requests, json
from dotenv import load_dotenv
from praw.models import MoreComments

load_dotenv()

access_token = ""

album_ids = []

track_ids = []

for album_id in album_ids:

    url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    tracks = response.json()

    # Iterate over the items in the response JSON and extract the track IDs
    for item in tracks['items']:
        track_ids.append(item['id'])


# Print the list of track IDs
print(track_ids)
