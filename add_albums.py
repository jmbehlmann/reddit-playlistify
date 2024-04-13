import praw, os, requests, json
from dotenv import load_dotenv
from praw.models import MoreComments

load_dotenv()

playlist_id = "5nt6uJH4N89CUMSOUnse3m"

access_token = "BQC0SaQhAdhnMJIuCwwZTDwcKrxwDL1SKFsQjll1fyQU52LextEaOok3SWVhkwPczoNvrvX5sIMYSCOGzbi_kVcUeuJLBioUellhcsDzjyTsCCxrqrOGMJhTZvnLWhT52HLP5BV2Pl-1YR9jVgJYiISs_xMYnGYWMUt8mYZE6uKfVRhDEeSApA9Pibw7FTLsXSKQ4_BtSAOXS5VsgHxk9bdja9nwcFZzTNPrjWl5M3JlZnbtp7ppt8RKqg"

track_ids = ['7K8mX41Nub7AzBt1RwwE6d', '55sPjd9D4VelNiR70Y1cCr', '3lhAQN2KNPh4G7RZ1hS5g5', '3oNP9Gh1NY4sjqaVUaNjTQ', '6AdyaWgJliC8HJU4CseNJM', '1BNZMXjqqULiV0DmFU1B8S']

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
if response.status_code == 201:
    print('Album added to playlist successfully!')
else:
    print('Failed to add album to playlist:', response.text)
