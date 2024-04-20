import praw, os, requests, json
from dotenv import load_dotenv
from praw.models import MoreComments

load_dotenv()

album_id = "2NnkLRaeX33d1Mn8ZLgTo8"

access_token = "BQCb7nd_mxOmxxSJZGoSI_LP9vbvFomCAge5OzgPVSMjmEK4KXB7VKm1RRrHsoYAoCiXrXDjqhaGGPcyywemBeV2tfGjwFT7slwgGOURiLMmD9x4Fr-O0IrxDdgE2b-0inKjo1YfEKiknkXfUDwdFc8QaELuDYvFrOM3oTWsyy3NyOyb92NnbBSTIS16QowKTfjHr-0V58eRnLuiU8VirZTyztpPWqyrWiFuj-2nOzHyU00UL-dyNRdvCQ"

url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get(url, headers=headers)

tracks = response.json()

track_ids = []

# Iterate over the items in the response JSON and extract the track IDs
for item in tracks['items']:
    track_ids.append(item['id'])

# Print the list of track IDs
print(track_ids)
