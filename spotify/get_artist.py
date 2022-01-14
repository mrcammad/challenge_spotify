import requests
import json
from fastapi import HTTPException, status
from config import settings
from spotify.get_token import GetToken

class GetArtist:

    def __init__(self):
        self.url = settings.URL
        token = GetToken()
        self.token = (token.get_token())["access_token"]
        self.headers = {'Authorization': f'Bearer {self.token}'}

    def get_artist(self,artist):
        try:
            url = self.url + f"/search/?q=artist:\"{artist}\"&type=artist"
            response = requests.request("GET", 
                                    url, 
                                    headers=self.headers, 
                                    data={}
                                )
            return json.loads(response.content)

        except:
            raise HTTPException (
                status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail = "ups! An error occurred with the artist"
            )