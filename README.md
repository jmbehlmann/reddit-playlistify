# Threadlistify

Threadlistify is a Python application that utilizes various APIs to retrieve data from Reddit threads, analyze comments, and interact with the Spotify API to create playlists based on mentioned albums.


## Features

- **Reddit Comment Analysis:** Retrieves top-level comments from a specified Reddit thread and analyzes them to extract mentioned albums.
- **OpenAI Integration:** Utilizes OpenAI's GPT-3.5 language model to process Reddit comments and extract album names.
- **Spotify Playlist Creation:** Interacts with the Spotify API to create playlists based on the extracted albums.
- **Environment Variable Configuration:** Utilizes environment variables for secure configuration of API credentials.

## Things you will need

- Reddit api credentials
- OpenAI api credentials
- Spotify api credentials

## Installation

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/your-username/threadlistify.git
    ```

2. Navigate to the project directory:

    ```
    cd threadlistify
    ```

3. Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. **Obtain Reddit API Credentials:**

   - Create a Reddit application and obtain the client ID, client secret, password, user agent, and username.

2. **Set Up Environment Variables:**

   - Create a `.env` file in the project directory.
   - Add the following environment variables to the `.env` file:
     ```
     CLIENT_ID=your_reddit_client_id
     CLIENT_SECRET=your_reddit_client_secret
     PASSWORD=your_reddit_password
     USER_AGENT=your_reddit_user_agent
     USERNAME=your_reddit_username
     OPENAI_KEY=your_openai_api_key
     SPOTIFY_CLIENT_ID=your_spotify_client_id
     SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
     SPOTIFY_AUTH_CODE=code_from_spotify_auth
     REDDIT_THREAD_URL=url_of_thread_you_want_to_threadlistify
     ```

3. **Authenticate with Spotify:**

    - Run the `spotify_auth.py` script to obtain the authorization code needed for accessing the Spotify API:

    ```bash
    python spotify_auth.py
    ```

    Follow the prompts to authenticate with Spotify. A browser window will open with a code in the url, add that code to the main function.

4. **Run the Main Application:**

    - Once you have obtained the Spotify authorization code, you can run the main application:

    ```bash
    python main.py
    ```

    The application will gather comments from a specified Reddit thread, extract album references, search for these albums on Spotify, and add them to a specified playlist.


## Dependencies

- [praw](https://github.com/praw-dev/praw)
- [requests](https://github.com/psf/requests)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [OpenAI API](https://openai.com/)
- [Spotify API](https://developer.spotify.com/documentation/web-api/)

## Contributing

Contributions are welcome! If you'd like to contribute to Threadlistify, please fork the repository and create a pull request.

## License

This project is licensed under the MIT License
