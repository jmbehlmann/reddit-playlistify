import praw, os, requests, json
from dotenv import load_dotenv
from praw.models import MoreComments

# get reddit comments from thread(top level comments only)

def get_reddit_comments(thread_url):
    print("getting reddit comments")

    load_dotenv()

    # client_id = os.environ.get('CLIENT_ID')
    # client_secret = os.environ.get('CLIENT_SECRET')
    # password = os.environ.get('PASSWORD')
    # user_agent = os.environ.get('USER_AGENT')
    # username = os.environ.get('USERNAME')

    reddit = praw.Reddit(
        client_id=os.environ.get('CLIENT_ID'),
        client_secret=os.environ.get('CLIENT_SECRET'),
        password=os.environ.get('PASSWORD'),
        user_agent=os.environ.get('USER_AGENT'),
        username=os.environ.get('USERNAME'),
    )

    url = thread_url
    submission = reddit.submission(url=url)
    title = submission.title
    # top level comments only
    print(title)
    comments = ""

    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        comments += top_level_comment.body.replace('\n', '') + " "

    print("got reddit comments")
    return(comments)


# send comments to openai to return artists and albums

def send_to_openai(comments):
    print("sending to openai")

    url = "https://api.openai.com/v1/chat/completions"
    openai_key = os.environ.get('OPENAI_KEY')

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(openai_key)
    }

    prompt = f"The following is a comment thread from reddit. Please find all of the albums referenced in the text and put them into a python list with both the artist and the album title combined into a single element in the list. Remove any duplicates so that each album only appears in the list once. You may need to remove any punctuation or any extra info so that each line is formatted as 'artist album'  {comments}"

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"{prompt}"}],
        "temperature": 0
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        # Parse the JSON response
        response_json = response.json()

        # Extract the content from the response
        content = response_json['choices'][0]['message']['content']

        # maybe change this to json.loads
        albums = eval(content)
        # print(albums[0])
    else:
        # Print an error message if the request failed
        print('Error:', response.text)

    print("received data from openai")
    return albums


# get album ids

def get_album_ids(albums, access_token):
    print("getting album ids")

    # Define the base URL for the Spotify API
    url = 'https://api.spotify.com/v1/search'

    album_ids = []

    for album in albums:

        # Define the search query
        query = album

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
            print(f"the album id for {album} is {album_id}")
            album_ids.append(album_id)
        else:
            # Print an error message if the request failed
            print("Failed to search for album:", response.text)

    return album_ids

def create_playlist():
    pass


# get track ids for each album
def add_to_playlist(album_ids, playlist_id, access_token):

    print("getting track ids")

    for album_id in album_ids:

        track_ids = []

        url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        response = requests.get(url, headers=headers)

        tracks = response.json()

        # Iterate over the items in the response JSON and extract the track IDs
        for item in tracks['items']:
            track_ids.append(item['id'])

        formatted_track_ids = []

        for track_id in track_ids:
            formatted_track_ids.append(f'spotify:track:{track_id}')

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
        print("added an album")

def main():

    code = ""

    access_token = "BQDnZFqQsF8JE6oIqnrKX-YYC_Abmn7pFaUaB_YgUKnaU_nJohiqQ1tb5wRv8csstUXetQf9ICWXUFI3JTKhHKqG25iVcdjnj8pS0sad5I3QjD8ArFYqvDrJBHjo3PMgWBMfZPeEiQ1PBz4o-lznh0qlZDAONWdMgYq92GyWgsERlR-fELSUFO3zF8zyGc3jsTD4aM-dWV4lhmtre6tBTckxNN83pJJtfz6OCpnt_kcS_J-ooKb57ko7ig"

    playlist_id = "5nt6uJH4N89CUMSOUnse3m"

    thread_url = "https://www.reddit.com/r/swans/comments/1c2n4y1/day_4_what_are_swans_fans_favorite_albums_outside/"

    comments = get_reddit_comments(thread_url)
    albums =  send_to_openai(comments)
    album_ids = get_album_ids(albums, access_token)
    # playlist_id = create_playlist()
    add_to_playlist(album_ids, playlist_id, access_token)

if __name__ == "__main__":
    main()
