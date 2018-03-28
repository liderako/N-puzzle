import numpy

class Matrix:
	def __init__(self, _size):
		self.size = _size
		self.matrix = numpy.zeros((_size, _size))

	def move_right(self,row,column):
		buf = self.matrix[row][column]
		self.matrix[row][column] = self.matrix[row][column + 1]
		self.matrix[row][column + 1] = buf
	def move_left(self,row,column):
		buf = self.matrix[row][column]
		self.matrix[row][column] = self.matrix[row][column - 1]
		self.matrix[row][column - 1] = buf
	def move_up(self,row,column):
		buf = self.matrix[row][column]
		self.matrix[row][column] = self.matrix[row - 1][column]
		self.matrix[row - 1][column] = buf
	def move_down(self,row,column):
		buf = self.matrix[row][column]
		self.matrix[row][column] = self.matrix[row + 1][column]
		self.matrix[row + 1][column] = buf
	def setMatrix(self, matrix):
		self.matrix = matrix
