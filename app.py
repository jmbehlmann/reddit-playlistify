import praw
import os
import requests

from dotenv import load_dotenv
from praw.models import MoreComments

load_dotenv()

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
password = os.environ.get('PASSWORD')
user_agent = os.environ.get('USER_AGENT')
username = os.environ.get('USERNAME')


reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password=password,
    user_agent=user_agent,
    username=username,
)

url = "https://www.reddit.com/r/swans/comments/1c21ed3/day_3_what_are_swans_fans_favorite_albums_outside/"
submission = reddit.submission(url=url)

# top level comments only

comments = ""

for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    comments += top_level_comment.body.replace('\n', '') + " "

# print(comments)


# all comments

# submission.comments.replace_more(limit=None)
# for comment in submission.comments.list():
#     print(comment.body)


url = "https://api.openai.com/v1/chat/completions"
openai_key = os.environ.get('OPENAI_KEY')

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(openai_key)
}



prompt = f"The following is a comment thread from reddit. Please find all of the albums referenced in the text and put them into a python dictionary. The key of each line should be the artist name and the value should be the album name. You may need to reorganize some of the comments in order to return a properly formatted dictionary:  {comments}"

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

    # Print or return the content
    print(content)
else:
    # Print an error message if the request failed
    print('Error:', response.text)
