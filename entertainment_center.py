import fresh_tomatoes
import media
import urllib
import json
import connect


movies_list = []

for item in connect.movie_query["items"]:

    movie_title = item["title"]

    movie_poster = "https://image.tmdb.org/t/p/w500{}".format(item["poster_path"])

    trailer_api = "http://api.themoviedb.org/3/movie/{}/videos?api_key={}".format(str(item["id"]), connect.api_key)
    trailer = urllib.urlopen(trailer_api)
    trailer = json.loads(trailer.read())
    movie_trailer = "https://youtu.be/{}".format(trailer["results"][0]["key"])

    movie_overview = item["overview"]

    item = media.Movie(movie_title,
                       movie_overview,
                       movie_poster,
                       movie_trailer)

    movies_list.append(item)

fresh_tomatoes.open_movies_page(movies_list)
