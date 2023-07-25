class Movie:
    '''
   Declaration a class called Movie ,, that generates an instance movie 
   with many properties such as title,year ,genres
    '''
    def __init__ (self, title, year, genres):
        self.title = title
        self.year = year
        self.genres = genres

    def __str__(self):# the method to print an instance 
        return f"Movie(title='{self.title}', year={self.year}, genres={self.genres})"


class MovieSorter:
    '''
    declaration class called moviesorter with staticmethods to be used outside the
    class
    '''
    @staticmethod
    def sort_ByYear_Descending(movies):
        sorted_movies = sorted(movies, key=lambda movie: movie.year, reverse=True)
        return sorted_movies

    @staticmethod
    def sort_Alphabetically_Ignoring_Articles(movies):
        def remove_leading_articles(title):
            articles = ["A ", "An ", "The "]
            for x in articles:
                if title.startswith(x):
                    return title[len(x):]
            return title

        sorted_movies = sorted(movies, key=lambda movie: remove_leading_articles(movie.title))
        return sorted_movies


