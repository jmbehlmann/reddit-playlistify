import praw, os, requests, json
from dotenv import load_dotenv
from praw.models import MoreComments

load_dotenv()

album_id = "2NnkLRaeX33d1Mn8ZLgTo8"

access_token = "BQC0SaQhAdhnMJIuCwwZTDwcKrxwDL1SKFsQjll1fyQU52LextEaOok3SWVhkwPczoNvrvX5sIMYSCOGzbi_kVcUeuJLBioUellhcsDzjyTsCCxrqrOGMJhTZvnLWhT52HLP5BV2Pl-1YR9jVgJYiISs_xMYnGYWMUt8mYZE6uKfVRhDEeSApA9Pibw7FTLsXSKQ4_BtSAOXS5VsgHxk9bdja9nwcFZzTNPrjWl5M3JlZnbtp7ppt8RKqg"

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
