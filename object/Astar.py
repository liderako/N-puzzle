import sys
from Rules import *
from State import *
import hashlib

class 	Astar:

# Creates an object to find the terminal state by the specified rules.
	def 	__init__( self, rules ):
		self.closedStates = 0
		self.rules = rules

# Applies the algorithm A * to find the shortest path to the terminal state from the indicated.
# return @param a sequence of states from a given state to a terminal state.
	def 	search( self, startState ):
		## step 1
		closeList = list()
		openList = list()
		## step 2
		openList.append( startState )
		startState.setG( 0 )
		startState.setH( self.rules.getH( startState ) )
		j = 0	

		while (len(openList)!= 0):
			## step 3
			xState,i = self.getStateWithMinF(copy.deepcopy(openList))
			xState.setG(self.rules.getDistance(copy.deepcopy(startState)))
			xState.setH(self.rules.getH(xState))
			## step 4
			if self.rules.isTerminate(copy.deepcopy(xState)):
				return self.completeSolution(xState)
			## step 5
			openList.pop(i)
			closeList.append(xState) 
			## step 6
			neighborsListState = self.rules.getNeighbors(copy.deepcopy(xState))
			for neighbor in neighborsListState:
				### step 7
				if ((self.find(neighbor, closeList)) == True):
					continue
				## step 8
				if ((self.find(neighbor, copy.deepcopy(openList)) == False)):
					yG = xState.getG() + self.rules.getDistance(copy.deepcopy(neighbor), copy.deepcopy(xState))
					neighbor.setG(yG)
					neighbor.setH(xState.getH())
					openList.append(copy.deepcopy(neighbor))
				else:
					g = xState.getG() + self.getDistance(neighbor, xState)
					if g < xState.getG():
						# xState.getG(g)
						# neighbor.setStateParent(co)
				# isGBetter = False
# 
				# if ((self.find(neighbor, copy.deepcopy(openList)) == False)):
					# openList.append(copy.deepcopy(neighbor))
				# else:
					# isGBetter = xState.getF() < neighbor.getF();
				# if (isGBetter):
					# neighbor.setStateParent(copy.deepcopy(xState))
					# neighbor.setG(g)
		## step 10
		return 0;

	def 	find(self, state, listState):
		i = 0
		res = 0
		size = state.getMatrixObject().getSize() * state.getMatrixObject().getSize()
		for currentState in listState:
			res = 0
			s = copy.copy(state.getMatrixArray())
			tmp = copy.copy(currentState.getMatrixArray())
			while (i < state.getMatrixObject().getSize()):
				j = 0
				while j < state.getMatrixObject().getSize():
					if (s[i][j] == tmp[i][j]):
						res += 1
					j += 1
				i += 1
			if (res == size):
				return True
		return (False)

#  Finds the vertex in the openList with the lowest weight value.
	def 	getStateWithMinF( self, openList ):
		min = sys.maxsize - 1
		i = 0
		res = State(Matrix(3))
		for state in openList:
			if state.getF() < min:
				min = state.getF()
				res = copy.deepcopy(state)
				i += 1
		return res, i - 1


# It is the sequence of states passed from the initial state to the final one.
	def 	completeSolution( self, terminate ):
		print ""
		print terminate.getMatrixArray()