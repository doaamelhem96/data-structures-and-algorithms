class Movie:
    def __init__(self, title, year, genres):
        self.title = title
        self.year = year
        self.genres = genres

    def __repr__(self):
        return f"Movie(title='{self.title}', year={self.year}, genres={self.genres})"


def sort_movies_by_year(movies):
    movies.sort(key=lambda movie: movie.year, reverse=True)
    return movies


def sort_movies_by_title(movies):
    def get_title_key(movie):
        title = movie.title
        if title.startswith("A "):
            return title[2:]
        elif title.startswith("An "):
            return title[3:]
        elif title.startswith("The "):
            return title[4:]
        return title

    movies.sort(key=get_title_key)
    return movies


movies = [
    Movie("The Avengers", 2012, ["Action", "Adventure"]),
    Movie("Anchorman: The Legend of Ron Burgundy", 2004, ["Comedy"]),
    Movie("A Beautiful Mind", 2001, ["Biography", "Drama"]),
]

# Sort movies by year
sorted_by_year = sort_movies_by_year(movies)
print(sorted_by_year)

# Sort movies by title
sorted_by_title = sort_movies_by_title(movies)
print(sorted_by_title)
