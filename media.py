# Defines the class Movie
class Movie():
    # The constructor takes in the movie title, poster, and trailer
    def __init__(self, title, poster, trailer):
        self.title = title
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
