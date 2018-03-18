import numpy

class Matrix:
	def __init__(self, _size):
		self.size = _size
		self.matrix = numpy.zeros((_size, _size))

	def move_right(row,column):
		buf = self.matrix[row][column]
		self.matrix[row][column] = self.matrix[row + 1][column]
		self.matrix[row + 1][column] = buf
	def move_left(row,column):
		buf = self.matrix[row][column]
		self.matrix[row][column] = self.matrix[row - 1][column]
		self.matrix[row + 1][column] = buf
	def move_up(row,column):
		buf = self.matrix[row][column]
		self.matrix[row][column] = self.matrix[row][column - 1]
		self.matrix[row][column - 1] = buf
	def move_down(row,column):
		buf = self.matrix[row][column]
		self.matrix[row][column] = self.matrix[row + 1][column]
		self.matrix[row + 1][column] = buf
