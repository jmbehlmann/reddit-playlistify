import praw
from dotenv import load_dotenv
import os

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

url = "https://www.reddit.com/r/swans/comments/1c17v50/day_2_what_are_swans_fans_favorite_albums_outside/"
submission = reddit.submission(url=url)


for top_level_comment in submission.comments:
    print(top_level_comment.body)
