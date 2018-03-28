from Matrix import *
class 	State:

	def __init__( self, matrix ):
		self.matrix = matrix

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
		return self.stateParent

	def setStateParent( self, stateParent ):
		self.stateParent = stateParent;

	def getMatrixArray( self ):
		return self.matrix.matrix