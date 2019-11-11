import pandas as pd
import random

dMovies = pd.read_csv('output/dfMovies.csv')
dTomatoe = pd.read_csv('output/dfTomatoe.csv')

def checkGenre(genre)

def chooseGenre(genre):
    import pandas as pd
    import random
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
    import pandas as pd
    moviereport = (dMovies[dMovies['title'] == movie])
    print (moviereport)
    return moviereport
    