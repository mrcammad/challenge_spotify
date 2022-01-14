import requests
import json
from fastapi import HTTPException, status
from config import settings
from spotify.get_artist import GetArtist
from spotify.get_token import GetToken

class GetAlbums:
    def __init__(self):
        self.url = settings.URL
        self.artist_data = GetArtist()
        token = GetToken()
        self.token = (token.get_token())["access_token"]
        self.headers = {'Authorization': f'Bearer {self.token}'}


    def get_albums(self,artist_name):

        artist = self.artist_data.get_artist(artist_name)

        if len(artist["artists"]["items"]) < 1:
            raise HTTPException (
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "ups! We did not find any album for this artist"
            )

        try:

            artist_id = artist["artists"]["items"][0]["id"]

            url = self.url + f"/artists/{artist_id}/albums?limit=50"

            response = requests.request("GET", 
                                            url, 
                                            headers=self.headers, 
                                            data={}
                                        )

            return json.loads(response.content)

        except:
            raise HTTPException (
                status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail = "ups! An error occurred with the albums"
            )
