import argparse
from functions import functions
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
​
	return parser.parse_args()

def start(genre,email):
    print("Looking for "+genre+" movie!\n")
	selectedGenre = chooseGenre(genre)
	
	print("I have a movie for you: -->"+selectedGenre+ "<-- It's my choice")
	
	moviereport = showMovie(selectedGenre)
	




def main():
    args = get_args()
    if args.mail and args.genre:
        genre = args.genre
        email = args.mail
        start(genre,email)
    elif args.mail:
        email = args.mail
        genre = input("Choose a genre: \n")
        start(genre,email)
    elif args.genre:
        genre = args.genre 
        email = input("Type the receiver mail:")
        start(genre,email)


if __name__=='__main__':
    main()