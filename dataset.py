import pandas as pd
import re

df = pd.read_csv('./src/movies_metadata.csv')

dfclean = df.drop(['popularity', 'id', 'adult', 'poster_path', 'spoken_languages', 'tagline', 'budget', 'vote_count', 'belongs_to_collection', 'homepage', 'imdb_id', 'production_companies', 'production_countries', 'revenue', 'status', 'video'], axis=1)

dfclean2 = dfclean.dropna()
dfclean2.count()

genresclean = []
for e in dfclean['genres']:
    e = str(re.sub("[^A-Za-z]","", e))
    e = str(re.sub('idname', ",", e))
    genresclean.append(e.strip(','))
    
dfclean['genres'] = genresclean

genresclean2 = []
for e in dfclean['genres']:
    if e == '':
        e = 'Uknkown'
        genresclean2.append(e)
    else:
        genresclean2.append(e)
dfclean['genres'] = genresclean2

dfclean.to_csv('./output/dfMovies.csv')