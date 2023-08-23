import json
import requests
from creden import username,playlist_id
from refresh import Refresh

class SpotifyHistory:
    def __init__(self):
        self.spotify_user_id = username
        self.playlist_id = playlist_id
        self.tracks = ""
        self.spotify_access_token = ""

    def find_songs(self):
        print("Finding recently played...")

        query = "https://api.spotify.com/v1/me/player/recently-played"

        response = requests.get(query,headers={"Content-Type":"application/json","Authorization":"Bearer {}".format(self.spotify_access_token)},params={"limit":50})

        response_json = response.json()

        for i in response_json["items"]:
            self.tracks += i["track"]["uri"] + ","
            print(i["track"]["name"])
        self.tracks = self.tracks[:-1]
        self.replace_songs()
    
    def replace_songs(self):
        print("Replacing songs in playlist...")

        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(self.playlist_id)

        response = requests.put(query,headers={"Content-Type":"application/json","Authorization":"Bearer {}".format(self.spotify_access_token)},params={"uris":self.tracks})

        print(response)
        print("Success!")
        


    def start(self):
        print("Refreshing token....")
        refreshCaller = Refresh()
        self.spotify_access_token = refreshCaller.refresh()
        self.find_songs()
    

a = SpotifyHistory()
a.start()