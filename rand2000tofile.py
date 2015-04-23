import random


def rand_2000_to_file():
	print "running"
	count = 0
	numeros = []
	while count < 2000:
		alt = random.randrange(1,2000)
		found = False
		for numero in numeros:
			if numero == alt:
				found = True
		if not found:
			print "%d -> %d" % (count, alt)
			numeros.append(alt)
			count=count+1

if __name__ == "__main__":
	rand_2000_to_file()
