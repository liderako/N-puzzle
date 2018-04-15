import sys
from Rules import *
from State import *

class 	Astar:

# Creates an object to find the terminal state by the specified rules.
	def 	__init__( self, rules ):
		self.closedStates = 0
		self.rules = rules

# Applies the algorithm A * to find the shortest path to the terminal state from the indicated.
# return @param a sequence of states from a given state to a terminal state.
	def 	search( self, startState ):
		closeList = list()
		openList = list()
		openList.append( startState )
		startState.setG( 0 )
		startState.setH( self.rules.getH( startState ) )
		while (len(openList)!= 0):
			current,i = self.getStateWithMinF(openList)
			if 	self.rules.isTerminate(current):
				return self.completeSolution(current)
			openList.pop(i)
			closeList.append(current) 
			neighborsListState = self.rules.getNeighbors(current)
			for next in neighborsListState:
				if ((self.find(next, closeList)) == True):
					continue
				if ((self.find(next, openList) == False)):
					next.setH(self.rules.getH(copy.deepcopy(next)))
					openList.append(next)		
				gScope = current.getG() + self.rules.getDistance(copy.deepcopy(current), copy.deepcopy(next))
				print self.rules.getDistance(copy.deepcopy(next), copy.deepcopy(current))
	
				if gScope >= next.getG():
					continue
				print "WTF"
				next.setG(gScope)
				next.setStateParent(current)
				# neighbor.parent = current
				# print "dasdas"
				# print neighbor.parent.getMatrixArray()
				# print neighbor.getStateParent()
		return 0;

 


	def 	find(self, state, listState):
		res = 0
		sizeLine = state.getMatrixObject().getSize()
		size = sizeLine * sizeLine
		s = state.getMatrixArray()
		for currentState in listState:
			res = 0
			tmp = currentState.getMatrixArray()
			i = 0
			while (i < sizeLine):
				j = 0
				while j < sizeLine:
					if (s[i][j] == tmp[i][j]):
						res += 1
					j += 1
				i += 1
			if (res == size):
				return True
		return (False)

	def 	getStateWithMinF( self, openList ):
		min = sys.maxsize - 1
		i = 0
		i_res = 0
		res = State(Matrix(openList[0].getMatrixObject().getSize()))
		for state in openList:
			if state.getF() <= min:
				min = state.getF()
				res = copy.deepcopy(state)
				i_res = i
			i += 1
		return res, i_res

	def 	completeSolution( self, terminate ):
		print "WTF"
		print terminate.getMatrixArray()
		# terminate.getStateParent()
		# print a.getMatrixArray()