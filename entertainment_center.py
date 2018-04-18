import fresh_tomatoes
import media


# Creates an instance of a movie where title, poster art, and trailer are provided
black_panther = media.Movie("Black Panther",
                            "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
                            "https://www.youtube.com/watch?v=xjDjIWPwcPU")

crows_zero = media.Movie("Crows Zero",
                         "https://upload.wikimedia.org/wikipedia/en/3/37/Crowszero.jpg",
                         "https://www.youtube.com/watch?v=Gjz8q60jI3w")

rurouni_kenshin = media.Movie("Rurouni Kenshin",
                              "https://upload.wikimedia.org/wikipedia/en/f/f6/Rurouni_Kenshin_%282012_film%29_poster.jpg",
                              "https://www.youtube.com/watch?v=bXkyJxyJT3E")

# Adds each movie instance into a list
movies = [black_panther, crows_zero, rurouni_kenshin]

# Creates movie tiles and opens the movie page
fresh_tomatoes.create_movie_tiles_content(movies)
fresh_tomatoes.open_movies_page(movies)
