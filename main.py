import argparse
import pandas as pd
from functions import chooseGenre
from functions import showMovie
from pdf import create_pdf
​
​
def parse():
	parser = argparse.ArgumentParser()                 # analizador de argumentos
	grupo = parser.add_mutually_exclusive_group()      # grupo mutuamente excluyente (solo una operacion)
​
	grupo.add_argument('-d', '--Drama', help='Search for drama movies.', action='store_true')           # action guarda el argumento
	grupo.add_argument('-c', '--Comedy', help='Search for comedy movies.', action='store_true')
	grupo.add_argument('-r', '--Romance', help='Search for romance movies.', action='store_true')
	grupo.add_argument('-h', '--Horror', help='Search for horror movies.', action='store_true')
    grupo.add_argument('-t', '--Thriller', help='Search for thriller movies.', action='store_true')
	
	parser.add_argument("-m", "--mail", type=str, help="Mail will receive the recommendation")
    args = parse.parse_args()
	print(args)
	return args

def start(genre, email):
    print("Looking for "+genre+" movie!\n")
	selectedGenre = chooseGenre(genre)
	
	print("I have a movie for you: -->"+selectedGenre+ "<-- It's my choice")
	
	moviereport = showMovie(selectedGenre)
    pdftosend = create_pdf(moviereport)


def main():
    args = parse()
    genre = args.genre
	dMovies = pd.read_csv('output/dfMovies.csv')
	dTomatoe = pd.read_csv('output/dfTomatoe.csv')


if __name__=='__main__':
    main()