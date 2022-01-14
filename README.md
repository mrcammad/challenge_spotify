challenge_spotify

El proyecto busca los albums de el artista que le indiquemos en la api de spotify.

Instalacion:

1. Debemos crear un ambiente virtual en nuesta maquina, con el comando "python3 -m venv venv"
2. Activar el ambiente virtual "source venv/bin/activate"
3. Luego debemos instalar el archivo requirements.txt , con el comando "pip3 install -r requirements.txt"
4. Una vez instalado el framework y las librerias debemos activar el servidor con el comando "uvicorn main:app --reload"
5. Para consumir el servicio lo debemos hacer en el endpoint con el metodo GET: http://127.0.0.1:8000/api/v1/albums?q={nombre_artista}

Documentacion en http://127.0.0.1:8000/docs
