#!python3

import csv
import random
from collections import defaultdict, namedtuple, Counter, deque
from urllib.request import urlretrieve

movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movies_csv = 'movies.csv'
urlretrieve(movie_data, movies_csv)

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(data=movies_csv):
    """Extracts all movies from csv and stores them in a dictionary where the keys are directors, and the values are a
        list of movies (named tuples)"""
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors


directors = get_movies_by_director()
print(directors)
# print(directors['Christopher Nolan'])

cnt = Counter()

for director, movies in directors.items():
    cnt[director] += len(movies)

# print(cnt.most_common(5))

# defaultdict(<class 'list'>, {'James Cameron': [Movie(title='Avatar', year=2009, score=7.9), Movie(title='Titanic', year=1997, score=7.7), Movie(title='Terminator 2: Judgment Day', year=1991, score=8.5), Movie(title='True Lies', year=1994, score=7.2), Movie(title='The Abyss', year=1989, score=7.6), Movie(title='Aliens', year=1986, score=8.4), Movie(title='The
# defaultdict(<class 'list'>, {'w3schools.comTHE': ['w3schools.comTHE'], "WORLD'S": ["WORLD'S"],