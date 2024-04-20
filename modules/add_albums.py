import praw, os, requests, json
from dotenv import load_dotenv
from praw.models import MoreComments

load_dotenv()

playlist_id = "5nt6uJH4N89CUMSOUnse3m"

access_token = "BQCb7nd_mxOmxxSJZGoSI_LP9vbvFomCAge5OzgPVSMjmEK4KXB7VKm1RRrHsoYAoCiXrXDjqhaGGPcyywemBeV2tfGjwFT7slwgGOURiLMmD9x4Fr-O0IrxDdgE2b-0inKjo1YfEKiknkXfUDwdFc8QaELuDYvFrOM3oTWsyy3NyOyb92NnbBSTIS16QowKTfjHr-0V58eRnLuiU8VirZTyztpPWqyrWiFuj-2nOzHyU00UL-dyNRdvCQ"

track_ids = ['7K8mX41Nub7AzBt1RwwE6d', '55sPjd9D4VelNiR70Y1cCr', '3lhAQN2KNPh4G7RZ1hS5g5', '3oNP9Gh1NY4sjqaVUaNjTQ', '6AdyaWgJliC8HJU4CseNJM', '1BNZMXjqqULiV0DmFU1B8S', '1WMawd1HhdmEojY4b1Ouyi', '27mFsmEWiSablfQTyZZhgp', '69xWltyIPMEXVzz3CcOKjq', '2TeMJxdraHOuzkK8AczQmK', '3DgH8JVn8baGEGi0PqOnFQ', '2PWAeDtnpreLIT8T5j8Gwx', '7kzgewBtUcnV2znGwzXLST', '36ImLZWNbfSrDwxrnJu5MW', '4WPhQssnzSr11cZFXtBJJo', '3AdjVNmizJU3o0UzoNTqe1', '3gnCUUpyd20COtouIAOMSJ', '6cU3yoD68fwfcUEqxgZUqP', '7FjB4s54iCaZHGUgTC50gd', '5v8lwej6qugmLPEqd6lPlF', '5mxbhYrlHsDZKZoHeTo4PD', '3WFNpbAcgVOrVyRYnWdSlm', '0yCnTG3dVkIPNSfhfVYQey', '7tewToewDkylbQLowEQOhG', '5pi2ZFJKx5fdlIcj4iwUPx', '6THlrOV1Aq6wVvJjZFTH5v', '1qHdxsdfe9DHV6YTitDARW', '1D2SVNlLeB4aHl5NlFKcBI', '5CQArxou1OKGWK5RMjISko', '0yRZBIFlSC1O2zZmIcCbup', '3c8UX4JbU8uNtcammOIFvo', '5K1E2khCTWeEwxN9jJw3Ws', '7c9CZGgrIEtrOJf3eBRYVz', '6j1LQhYnQR3McqO8U9N6EE', '63pdDeLroRpaT5uT805Q8M', '05vJCKdsaIdcMH5Vz53t5Q', '4eWZDgaawyC8nOrvp59alW', '1EQCSI0CSSE61nANLP4974', '46xnrF6T0XgKEFo0Yc9Dnv', '5dN3BuzeA9gIzEjUx501GD']

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
