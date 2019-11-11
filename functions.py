import pandas as pd
import random

dMovies = pd.read_csv('output/dfMovies.csv')
dTomatoe = pd.read_csv('output/dfTomatoe.csv')

def chooseGenre(genre):
    dtlist=dTomatoe[genre].tolist()
    dflist=dMovies['title'].tolist()
    while True:
        movie = random.choice(dtlist)
        if movie in dflist:
            print (movie)
            return movie
            break
        else:
            continue
    



def showMovie(movie):
    report = (dMovies[dMovies['title'] == movie])
    return report
    