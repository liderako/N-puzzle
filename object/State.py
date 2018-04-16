from Matrix import *

class 	State:

	def __init__( self, matrix ):
		self.matrix = matrix
		self.g = 0
		self.h = 0
		self.f = 0
		self.countParent = 0

	def getG( self ):
		return self.g;

	def getF( self ):
		return self.g + self.h;

	def getH( self ):
		return self.h

	def setH( self, h ):
		self.h = h;

	def setG( self, g ):
		self.g = g;

	def getStateParent( self ):
		return self.parent

	def setStateParent( self, stateParent ):
		self.countParent += 1
		self.parent = stateParent

	def getMatrixArray( self ):
		return self.matrix.matrix

	def getMatrixObject( self ):
		return self.matrix