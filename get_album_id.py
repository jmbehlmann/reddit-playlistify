import praw, os, requests, json
from dotenv import load_dotenv
from praw.models import MoreComments

load_dotenv()


# get album id

# Define the base URL for the Spotify API
url = 'https://api.spotify.com/v1/search'


# album = "Rubber Soul"
# artist = "Beatles"
# Define the search query
album = albums[19]
query = f'{album}'

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
else:
    # Print an error message if the request failed
    print("Failed to search for album:", response.text)

url = "https://api.spotify.com/v1/me"
headers = {
    "Authorization": f'Bearer {access_token}'
}

response = requests.get(url, headers=headers)

print(response.json())
