import sys
import argparse


def parse():
	parser = argparse.ArgumentParser(description='Choose a Genre, get a recommendation in your email')
	parser.add_argument('genre', help='Search for a genre movies.', default='Horror')           # action guarda el argumento
	parser.add_argument("mail", help="Mail will receive the recommendation")
	args = parser.parse_args()
	print(args)
	return args


def main():
	args = parse()
	import pandas as pd
	from functions import chooseGenre
	from functions import showMovie
	from pdf import createPDF
	from mail import checkMail
	from mail import sendMail
	print(sys.argv)
	genre = args.genre
	email = args.mail
	movie = chooseGenre(genre)
	moviereport = showMovie(movie)
	pdf = createPDF(moviereport)
	print('You have a movie recommendation report')
	if args.mail != None:
		mail = checkMail(args.mail)
		sendMail(mail,pdf)
	else:
		print('You have the report in the path: {}'.format(doc[0]))



if __name__=='__main__':
    main()