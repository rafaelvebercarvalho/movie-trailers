import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/pt/d/dc/Movie_poster_toy_story.jpg",
                        "https://youtu.be/rNk1Wi8SvNc")

avatar = media.Movie("Avatar",
                     "A story of a marine with love with some aliens",
                     "https://upload.wikimedia.org/wikipedia/pt/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/5PSNL1qE6VY")

interestelar = media.Movie("Interestelar",
                           "Story of a crazy astronaut",
                           "https://upload.wikimedia.org/wikipedia/pt/3/3a/Interstellar_Filme.png",
                           "https://youtu.be/BYUZhddDbdc")

movies = [toy_story, avatar, interestelar]
fresh_tomatoes.open_movies_page(movies)

