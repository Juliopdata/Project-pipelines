import sys
import argparse
import pandas as pd
from functions import chooseGenre
from functions import showMovie
from functions import checkGenre
from pdf import createPDF
from mail import checkMail
from mail import sendMail
import subprocess


def parse():
	parser = argparse.ArgumentParser(description='Choose a Genre, get a recommendation in your email')
	parser.add_argument('genre', help='Choose: comedy, romance, drama, horror or thriller', default='Horror')           # action guarda el argumento
	parser.add_argument('mail', help="Mail will receive the recommendation")
	args = parser.parse_args()
	print(args)
	return args


def main():
	args = parse()
	print(sys.argv)
	genre = args.genre
	email = args.mail
	genre = checkGenre(genre)
	movie = chooseGenre(genre)
	moviereport = showMovie(movie)
	pdf = createPDF(moviereport)
	print('You have a movie recommendation report')
	if args.mail != None:
		mail = checkMail(args.mail)
		sendMail(mail,pdf)
		print ("The movie recommendation has been sent to {}".format(email))
	else:
		print('You have the report in the path: {}'.format(moviereport[0]))
	text = '"DING, DONG, YOU HAVE AN EMAIL"'
	subprocess.call('espeak -vF4 '+text, shell=True)

if __name__=='__main__':
    main()