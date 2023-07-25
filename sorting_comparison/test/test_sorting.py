import pytest
from sorting import Movie, MovieSorter


@pytest.fixture
def movies():
    return [
        Movie("The Matrix", 2012, ["Action", "Sci-Fi"]),
        
        Movie("A New Movie 1", 2021, ["Action", "Adventure"]),
    ]


def test_sort_ByYear_Descending(movies):
    sorted_movies = MovieSorter.sort_ByYear_Descending(movies)
    years = [movie.year for movie in sorted_movies]
    assert years == [2021, 2012]


def test_sort_Alphabetically_Ignoring_Articles(movies):
    sorted_movies = MovieSorter.sort_Alphabetically_Ignoring_Articles(movies)
    titles = [movie.title for movie in sorted_movies]
    assert titles == ["The Matrix", "A New Movie 1"]