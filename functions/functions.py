import pandas as pd

dMovies = pd.read_csv('output/dfMovies.csv')
dTomatoe = pd.read_csv('output/dfTomatoe.csv')

def chooseGenre(genre):
    movie = dfTomatoe[genre].sample(n = 1)
    return movie


def showMovie(movie):
     report = (dfclean[dfclean['title'] == movie])

