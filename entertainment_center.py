import fresh_tomatoes
import media
import urllib
import json
import connect

# Estanciando uma array para enviar no final
movies_list = []
# Esse FOR foi criado para receber os JSON e tratar eles para o HTML
for item in connect.movie_query["items"]:
    # Pegando o titulo do filme
    title = item["title"]
    # Pegado o poster
    poster = "https://image.tmdb.org/t/p/w500{}".format(item["poster_path"])
    # Para pegar o trailer, usaremos a API novamente, pegando o id do filme
    trailer_url = "http://api.themoviedb.org/3/movie/{}/videos?api_key={}"
    # Com a id, fazendo outra requisicao, trazendo agora o trailer
    trailer_api = trailer_url.format(str(item["id"]), connect.api_key)
    # Abrindo o JSON
    trailer = urllib.urlopen(trailer_api)
    # Lendo o JSON
    trailer = json.loads(trailer.read())
    # E do JSON extraimos a key do youtube do trailer
    movie_trailer = "https://youtu.be/{}".format(trailer["results"][0]["key"])
    # Pegando o resumo do filme
    overview = item["overview"]
    # Inserindo todos os dados obtidos dentro do item
    item = media.Movie(title,
                       overview,
                       poster,
                       movie_trailer)
    # Populando a array
    movies_list.append(item)
# Por fim, envindo para o fresh_tomatoes para criar a HTML
fresh_tomatoes.open_movies_page(movies_list)
