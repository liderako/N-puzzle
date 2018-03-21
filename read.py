import sys
from object.Matrix import *
import numpy as np
from astaralgo import *
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
	if (len(resultRead[0])) == 1 and resultRead[0] == ' ':
		del resultRead[0]
	for x in resultRead:
		try:
			resultRead.remove('')
		except:
			pass
	try:
		resultRead.remove('')
	except:
		pass
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
	m = createMatrix(res)
	return m

def 	createMatrix(list):
	m = Matrix(int(list[0]))
	sizeX = len(list[1])
	y = 0
	x = 0
	start = 0
	for x in list:
		if start == 0:
			start += 1
			pass
		else:
			s = x.split(' ')
			x = 0
			for n in s:
				m.matrix[y][x] = int(n)
				x += 1
			y += 1
	return m

resultRead = readFile(sys.argv[1])
m = convertInMatrix(resultRead)
#print m.matrix


'''
def     search_zero_indices(matryx):
        for i,j in enumerate(matryx):
                for k,l in enumerate(j):
                        if l==0:
				return i,k
'''
#print np.nanargmin(m.matrix, axis=None)

row,column = search_zero_indices(m.matrix)
print check_solve(m.matrix)

'''
m.move_right(row,column)
print m.matrix
row,column = search_zero_indices(m.matrix)
m.move_up(row,column)
print m.matrix
row,column = search_zero_indices(m.matrix)
m.move_left(row,column)
print m.matrix
row,column = search_zero_indices(m.matrix)
m.move_down(row,column)
print m.matrix
'''
