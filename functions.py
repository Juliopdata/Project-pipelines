import pandas as pd
import random

dMovies = pd.read_csv('output/dfMovies.csv')
dTomatoe = pd.read_csv('output/dfTomatoe.csv')

def chooseGenre(genre):
    dflist=dTomatoe[genre].tolist()
    return (random.choice(dflist))



def showMovie(movie):
    report = (dMovies[dMovies['title'] == movie])
    return report
    

