# Movie Trailer Website

This program takes in movie titles, poster art, and trailers and displays them on a website, allowing you to click each poster art to view the trailer for each movie.

## How to Use

1. Open **entertainment.py** and assign instances of the Movie class into variables.

```
example_movie1 = media.Movie("title", "url to the poster image", "url to the youtube trailer")
```

2. Add each movie variable into the movies list

```
movies = [example_movie1, example_movie2, example_movie3]
```

3. The list variable, `movies` is then taken by the following functions:

```
fresh_tomatoes.create_movie_tiles_content(movies)
fresh_tomatoes.open_movies_page(movies)
```

When run, these funcitons will create the movie tiles and open up the page in your web browser.
