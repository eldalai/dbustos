import random
import pdb


def rand_2000_to_file():
	print "running"
	count = 0
	numeros = range(1, 2001)
	salida = list()
	while count < 2000:
		posicion = random.randrange(0,2000-count)
		numero = numeros[posicion]
		del numeros[posicion]
		salida.append(numero)
		count=count+1
		print "%d -> %d" % (count, numero)		

if __name__ == "__main__":
	rand_2000_to_file()
