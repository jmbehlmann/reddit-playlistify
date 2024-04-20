import praw, os, requests, json
from dotenv import load_dotenv
from praw.models import MoreComments
load_dotenv()

comments = ""

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
    # Print or return the content
else:
    # Print an error message if the request failed
    print('Error:', response.text)
