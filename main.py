import argparse
​
​
def drama(a):        # funcion suma
	return a + b
​
def comedy(a):       # funcion resta
	return a - b
​
def romance(a):       # funcion multiplicacion
	return a * b
​
def horror(a):        # funcion division
	return a / b

def thriller(a):

​
def parse():
	parser = argparse.ArgumentParser()                 # analizador de argumentos
	grupo = parser.add_mutually_exclusive_group()      # grupo mutuamente excluyente (solo una operacion)
​
	grupo.add_argument('-d', '--drama', help='Search for drama movies.', action='store_true')           # action guarda el argumento
	grupo.add_argument('-c', '--comedy', help='Search for comedy movies.', action='store_true')
	grupo.add_argument('-r', '--romance', help='Search for romance movies.', action='store_true')
	grupo.add_argument('-h', '--horror', help='Search for horror movies.', action='store_true')
    grupo.add_argument('-t', '--thriller', help='Search for thriller movies.', action='store_true')
	
	parser.add_argument('y1', help='Choose a year', type=float)	
​
	return parser.parse_args()