from fastapi import FastAPI, Query
from spotify.get_albums_by_artist import GetAlbumByArtist

app = FastAPI()

@app.get('/api/v1/albums')
def get_albums_data( q : str = Query(...,
                                    title = "albums",
                                    description = "Name of the band",
                                    max_length = 100
                                    )
                    ):
    try:
        
        album_artist = GetAlbumByArtist()
        albums = album_artist.get_all_albums(q)
        return albums

    except Exception as e:
        raise e

