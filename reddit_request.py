import praw, os, requests, json
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

url = "https://www.reddit.com/r/swans/comments/1c2n4y1/day_4_what_are_swans_fans_favorite_albums_outside/"
submission = reddit.submission(url=url)
title = submission.title
# top level comments only

comments = ""

for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    comments += top_level_comment.body.replace('\n', '') + " "

# all comments

# submission.comments.replace_more(limit=None)
# for comment in submission.comments.list():
#     print(comment.body)

# print(comments)
