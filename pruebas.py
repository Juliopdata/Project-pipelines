import pandas as pd
import functions

def start(genre):
	print("Looking for "+genre+" movie!\n")
	selectedGenre = chooseGenre(genre)
	print("I have a movie for you:"+selectedGenre+"It's my choice")
	moviereport = showMovie(selectedGenre)

start('Drama')