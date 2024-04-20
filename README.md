# Threadlistify

Threadlistify is a Python application that utilizes various APIs to retrieve data from Reddit threads, analyze comments, and interact with the Spotify API to create playlists based on mentioned albums.

## Features

- **Reddit Comment Analysis:** Retrieves top-level comments from a specified Reddit thread and analyzes them to extract mentioned albums.
- **OpenAI Integration:** Utilizes OpenAI's GPT-3.5 language model to process Reddit comments and extract album names.
- **Spotify Playlist Creation:** Interacts with the Spotify API to create playlists based on the extracted albums.
- **Environment Variable Configuration:** Utilizes environment variables for secure configuration of API credentials.

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

1. Set up your environment variables by creating a `.env` file in the project directory. Include the following variables:

    ```
    CLIENT_ID=your_client_id
    CLIENT_SECRET=your_client_secret
    PASSWORD=your_reddit_password
    USER_AGENT=your_user_agent
    USERNAME=your_reddit_username
    OPENAI_KEY=your_openai_key
    ```

2. Run the main Python script to start the application:

    ```
    python main.py
    ```

3. Follow the prompts to authorize the application, specify the Reddit thread URL, and complete the process.

## Dependencies

- [praw](https://github.com/praw-dev/praw)
- [requests](https://github.com/psf/requests)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [OpenAI API](https://openai.com/)
- [Spotify API](https://developer.spotify.com/documentation/web-api/)

## Contributing

Contributions are welcome! If you'd like to contribute to Threadlistify, please fork the repository and create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
