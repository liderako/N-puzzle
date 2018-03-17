import numpy

class Matrix:
	def __init__(self, _size):
		self.size = _size
		self.matrix = numpy.zeros((_size, _size))