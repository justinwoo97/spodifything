from os import environ 
import spotipy
from urllib.parse import urlencode
import base64
import requests


# def get_artist_songs(sp,ids):
#     return artist_top_tracks(ids,country="US")

class Auth:
    def __init__(self,client_id,client_secret):
        self.client_id =client_id
        self.client_secret = client_secret

    def get_client_credentials(self,client_id,client_secret):
            """
            Returns a base64 encoded string
            """
            client_creds = f"{client_id}:{client_secret}"
            client_creds_b64 = base64.b64encode(client_creds.encode())
            return client_creds_b64.decode()

    def get_token_headers(self):
            client_creds_b64 = self.get_client_credentials(client_id,client_secret)
            return {
                "Authorization": f"Basic {client_creds_b64}"
            }

    def get_token_data(self):
            return {
                "grant_type": "client_credentials"
            } 



if __name__ == "__main__":
    ids = "13ubrt8QOOCPljQ2FL1Kca"
    token_url='https://accounts.spotify.com/api/token'
    client_id="bcc5d68787b04d459ca856b5b483b4fd"
    client_secret="824b71136b594ba2863d6c6a28924ac9"
    auth = Auth(client_id,client_secret)
    token_data = auth.get_token_data()
    token_headers = auth.get_token_headers()
    r = requests.post(token_url, data=token_data, headers=token_headers)
    data = r.json()
    access_token = data['access_token']
    print(access_token)
    headers = {
    "Authorization": f"Bearer {access_token}"
    }

    # the following code will find the top-tracks for the given artist (ASAP rocky)
    endpoint = "https://api.spotify.com/v1/artists"
    artist_url_Arocky ="13ubrt8QOOCPljQ2FL1Kca"
    artist_url_drake = "3TVXtAsR1Inumwj472S9r4"
    market=urlencode({'market':'US'})
    #     print(market)
    lookup_url = f"{endpoint}/{artist_url_drake}/top-tracks?{market}"
    print(lookup_url)
    r = requests.get(lookup_url, headers=headers)
    print(r.status_code)
    for x in range(10):
        tracks_name = r.json()["tracks"][x]["album"]["name"]
        print(tracks_name)

    # the following code will find 10 related-artists to Drake
    endpoint = "https://api.spotify.com/v1/artists"
    data ="13ubrt8QOOCPljQ2FL1Kca"
    lookup_url = f"{endpoint}/{data}/related-artists"
    # print(lookup_url)
    r = requests.get(lookup_url, headers=headers)
    for x in range(20):
        related_artists = r.json()["artists"][x]["name"]
        print(related_artists)
            