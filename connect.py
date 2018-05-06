import urllib
import json

# Aqui estao a key da api eo numero de uma lista publica
api_key = "43dde1c97f419b11987d5c6afa1a603a"
user_list = "64925"
# Aqui fazemos a query, usando a key ea lista, deixando pronto para ser usado
movie_query = urllib.urlopen(
    'https://api.themoviedb.org/3/list/{}?api_key={}'.format
    (user_list, api_key))
movie_query = json.load(movie_query)
