import pandas as pd
import re
df = pd.read_csv('./src/movies_metadata.csv')
dfclean = df.drop(['popularity', 'id', 'spoken_languages', 'tagline', 'budget', 'vote_count', 'belongs_to_collection', 'homepage', 'imdb_id', 'production_companies', 'production_countries', 'revenue', 'status', 'video'], axis=1)
