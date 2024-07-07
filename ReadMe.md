# Spotify Recent Tracks Playlist Updater

This Python script uses the Spotify API to update a playlist with the last 50 songs you have listened to on Spotify. It is perfect for creating a dynamic playlist that always reflects your recent listening habits.

## Prerequisites

- Python 3.x
- Spotify Developer Account

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/sumanbmondal/spotifyauto.git
    cd spotifyauto
    ```

2. **Install the required packages:**

    ```sh
    pip install requests spotipy
    ```

3. **Spotify Developer Dashboard Configuration:**
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
   - Create a new application to get your `Client ID` and `Client Secret`.
   - Add `http://localhost:8888/callback` as a Redirect URI in your application settings.

4. **Obtain your Refresh Token and Base64 Client Credentials:**

    - Follow [this guide](https://developer.spotify.com/documentation/general/guides/authorization-guide/#authorization-code-flow) to obtain your refresh token. 
    - Convert your `Client ID` and `Client Secret` to Base64 as follows:
      ```python
      import base64
      client_id = 'YOUR_CLIENT_ID'
      client_secret = 'YOUR_CLIENT_SECRET'
      base64_credentials = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
      print(base64_credentials)
      ```

5. **Configure your script:**

    Open `main.py` and update the following variables with your information:

    ```python
    refresh_token = "YOUR_REFRESH_TOKEN"
    base_64 = "YOUR_CLIENT_ID_IN_BASE_64"
    username = "USERNAME"
    playlist_id = "PLAYLIST_ID"
    ```

6. **Run the script:**

    ```sh
    python main.py
    ```

## main.py

Here is a brief overview of what `main.py` does:

- Authenticates with the Spotify API using your refresh token.
- Retrieves the last 50 songs you have listened to.
- Updates the specified playlist with these songs, ensuring it always contains your most recent tracks.

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/)
