import requests
import json 
from fastapi import HTTPException, status
from config import settings

class GetToken:

    def __init__(self):
        self.content_type = settings.TOKEN_CONTENT_TYPE
    
    def get_token(self):
        try:
            url = settings.URL_TOKEN_SPOTIFY

            response = requests.request("POST", 
                                        url, 
                                        headers={
                                                'Authorization': settings.AUTHORIZATION_TOKEN,
                                                'Content-Type': self.content_type
                                                }, 
                                        data={}
                                        )

            return json.loads(response.content)

        except:
            raise HTTPException (
                status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail = "ups! An error occurred with the token"
            )
