import sys
from Rules import *
from State import *

class 	Astar:

# Creates an object to find the terminal state by the specified rules.
	def 	__init__( self, rules ):
		self.closedStates = 0
		self.rules = rules

# Applies the algorithm A * to find the shortest path to the terminal state from the indicated.
	def 	search( self, startState ):
		# return @param a sequence of states from a given state to a terminal state.

		closeList = list()
		openList = list()
		openList.append( startState )
		startState.setG( 0 )
		startState.setH( self.rules.getH( startState ) )

		while (len(openList) != 0):
			x = self.getStateWithMinF( openList )
			print "before if"
			if self.rules.isTerminate( x ):
				# closedStates = len(closeList)
				return self.completeSolution(x)
			print "after if"
			break ;
			# openList.remove(x)

#  Finds the vertex in the openList with the lowest weight value.
	def 	getStateWithMinF( self, openList ):
		print "getStateWithMinF"
		min = -sys.maxsize - 1
		res = State()
		for state in openList:
			if (state.getH() < min):
				min = state.getH()
				res = state
		return res

# It is the sequence of states passed from the initial state to the final one.
	def 	completeSolution( self, terminate ):
		pass

startState = State()
rules = Rules()

a = Astar(rules)
a.search(startState)
