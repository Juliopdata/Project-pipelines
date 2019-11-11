import pandas as pd
import random

dMovies = pd.read_csv('output/dfMovies.csv')
dTomatoe = pd.read_csv('output/dfTomatoe.csv')
listgenres = ['drama', 'horror', 'comedy', 'thriller', 'romance']




def checkGenre(genre):
    while True:
        if genre in listgenres:
            return genre
            break
        else:
            genre=input("Please choose a movie genre: drama, horror, comedy, thriller or romance ")


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
    