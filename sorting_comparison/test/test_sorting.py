from sorting import Movie, sort_movies_by_year, sort_movies_by_title
import pytest

def test_sort_movies_by_year():
    movies = [
        Movie("The Avengers", 2012, ["Action", "Adventure"]),
        Movie("Anchorman: The Legend of Ron Burgundy", 2004, ["Comedy"]),
        Movie("A Beautiful Mind", 2001, ["Biography", "Drama"]),
    ]
    sorted_movies = sort_movies_by_year(movies)
    assert sorted_movies == [
        Movie("The Avengers", 2012, ["Action", "Adventure"]),
        Movie("Anchorman: The Legend of Ron Burgundy", 2004, ["Comedy"]),
        Movie("A Beautiful Mind", 2001, ["Biography", "Drama"]),
    ]

def test_sort_movies_by_title():
    movies = [
        Movie("The Avengers", 2012, ["Action", "Adventure"]),
        Movie("Anchorman: The Legend of Ron Burgundy", 2004, ["Comedy"]),
        Movie("A Beautiful Mind", 2001, ["Biography", "Drama"]),
    ]
    sorted_movies = sort_movies_by_title(movies)
    assert sorted_movies == [
        Movie("A Beautiful Mind", 2001, ["Biography", "Drama"]),
        Movie("Anchorman: The Legend of Ron Burgundy", 2004, ["Comedy"]),
        Movie("The Avengers", 2012, ["Action", "Adventure"]),
    ]
