import sys

class 	Astar:

# Creates an object to find the terminal state by the specified rules.
	def 	__init__( self, rules ):
		# self.min = -sys.maxsize - 1
		self.rules = rules

# Applies the algorithm A * to find the shortest path to the terminal state from the indicated.
	def 	search( self, startState ):
		# return @param a sequence of states from a given state to a terminal state.
		pass

#  Finds the vertex in the openList with the lowest weight value.
	def 	getStateWithMinF( self, openList ):
		min = -sys.maxsize - 1
		for state in openList:
			if (state.getH() < min):
				min = state.getH()
				res = state
		return res

# It is the sequence of states passed from the initial state to the final one.
	def 	completeSolution( self, terminate ):
		pass