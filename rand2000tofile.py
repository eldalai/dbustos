# importar modulos
import random
import pdb


def rand_2000_to_file():
	print "running"
	count = 0
	# genera un array de 2000 posiciones
	# con numeros de 1 al 2000. El limite superior se excluye
	numeros = range(1, 2001)
	# esta es una lista de salida... por ahora 
	salida = list()
	# se abre y crea el archivo de salida. 
	# el segundo parametro es para crear el archivo cada vez
	f = open('workfile.txt', 'w')
	# es para hacer un debug del proceso...
	#pdb.set_trace()
	while count < 2000:
		# genera un random entre 0 y 2000 - count
		posicion = random.randrange(0,2000-count)
		# saca el elemento de la posicion, 
		# los arrays empiezan en 0
		numero = numeros[posicion]
		# se elimina el elemento del array que elegimos antes
		del numeros[posicion]
		# agregamos el numero a la salida... 
		# por ahora es al pedo, 
		# pero como para que veas otra estructura en memoria
		salida.append(numero)
		count=count+1
		# se muestra en pantalla
		print "%d -> %d" % (count, numero)
		# se escribe en el archivo		
		f.write("%d -> %d\n" % (count, numero))


if __name__ == "__main__":
	# comienzo del programa
	rand_2000_to_file()
