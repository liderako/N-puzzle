import sys


## other file
import numpy

class Matrix:
	def __init__(self, _size):
		self.size = _size
		self.matrix = numpy.zeros((_size, _size))
## other file

def 	printError(string):
	print string
	sys.exit(1)

def 	readFile(nameFile):
	try:
		f = open(nameFile, 'r')
		res = f.read()
		return res.split('\n')
	except:
		printError("Read file error.")

def 	deleteSpace(resultRead):
	string = ''
	i = 0
	size = len(resultRead)
	try:
		for x in resultRead:
			if ((len(x)) == 1 and x[0] == ' '):
				pass
			else:
				string = string + x
				if (i + 1 != size):
					string = string + "\n"
			i += 1
		string = string.split('\n')
		return string
	except:
		printError("Error in deleteSpace.")

def 	validation(string):
	if (len(string[0])) != 1:
		printError("Error size map")
	# for c in string:
		# 
def 	convertInMatrix(resultRead):
	i = 0
	for c in resultRead:
		res = c.find("#")
		if (res == -1):
			pass
		elif (res == 0):
			resultRead[i] = " "
		else:
			printError("Error string in #")
		i += 1
	res = deleteSpace(resultRead)
	validation(res)
	print res
resultRead = readFile(sys.argv[1])
convertInMatrix(resultRead)
