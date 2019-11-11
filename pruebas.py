import pandas as pd
from functions import chooseGenre
from functions import showMovie

def start(genre):
	print("Looking for "+genre+" movie!\n")
	selectedGenre = chooseGenre(genre)	
	print("I have a movie for you: -->"+selectedGenre+ "<-- It's my choice")
	moviereport = showMovie(selectedGenre)
	print(moviereport)
	


start('Drama')