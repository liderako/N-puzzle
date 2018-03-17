import sys
from object.Matrix import *
# from libft.Error import *
# from libft.readFile import *
# from libft.isInt import *

def 	Error(string):
	print string
	sys.exit(1)

def isInt(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
    return True

def 	readFile(nameFile):
	try:
		f = open(nameFile, 'r')
		res = f.read()
		return res.split('\n')
	except:
		Error("Read file error.")

def 	deleteSpace(resultRead):
	string = ''
	i = 0
	size = len(resultRead)
	try:
		for x in resultRead:
			if ((len(x)) == 1 and x[0] == ' '):
				pass
			else:
				old = '0'
				for k in x:
					if k == ' ' and old != ' ':
						string = string + k
						old = ' '
					elif k != ' ':
						old = '0'
						string = string + k
				if (i + 1 != size):
					string = string + "\n"
			i += 1
		string = string.split('\n')
		return string
	except:
		Error("Error in deleteSpace.")

def 	validation(string):
	if (isInt(string[0])) == False:
		Error("Error size map")
	sizeMatrix = int(string[0])
	validationSizeLineHeight(sizeMatrix, string)
	validationSizeLineWeight(sizeMatrix, string)

def 	validationSizeLineHeight(sizeMatrix, string):
	start = 0
	y = 0
	for c in string:
		if (start == 0):
			start += 1
		else:
			if ((len(c)) >= 1 and c[0] != ' '):
				y += 1
			elem = c.split(' ')
			if (y > sizeMatrix):
				Error("Too big hight matrix")

def 	validationSizeLineWeight(sizeMatrix, string):
	pass

def 	convertInMatrix(resultRead):
	i = 0
	for c in resultRead:
		res = c.find("#")
		if (res == -1):
			pass
		elif (res == 0):
			resultRead[i] = " "
		else:
			Error("Error string in #")
		i += 1
	res = deleteSpace(resultRead)
	validation(res)

resultRead = readFile(sys.argv[1])
convertInMatrix(resultRead)
