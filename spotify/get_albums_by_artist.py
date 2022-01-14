from tkinter import EXCEPTION
from fastapi import HTTPException, status
from spotify.get_albums import GetAlbums

class GetAlbumByArtist:
    def __init__(self):
      self.albums_data = GetAlbums()

    def get_all_albums(self,artist_name):

        try:
            album_response = self.albums_data.get_albums(artist_name)

            albums = album_response["items"]
            all_albums = []
            for album in albums:
                all_albums.append(
                    {
                    "name": album["name"],
                    "released": album["release_date"],
                    "tracks": album["total_tracks"],
                    "cover": album["images"][0] 

                    }
                )
            return all_albums
            
        except Exception as e:
            raise e
