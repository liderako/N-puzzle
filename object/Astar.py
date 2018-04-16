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
		startState.setH( self.rules.getH( startState ))
		sizeLine = startState.getMatrixObject().getSize()
		size = sizeLine * sizeLine
		while (len(openList)!= 0):
			current,i = self.getStateWithMinF(openList)
			if 	self.rules.isTerminate(current):
				listState = list()
				return self.completeSolution(current,listState)
			openList.pop(i)
			closeList.append(current) 
			neighborsListState = self.rules.getNeighbors(current)
			for next in neighborsListState:
				if ((self.find(next, closeList, size, sizeLine)) == True):
					continue
				gScope = current.getG() + 1
				isGBetter = False
				if ((self.find(next, openList, size, sizeLine) == False)):
					next.setH(self.rules.getH(next))
					openList.append(next)
					isGBetter = True		
				else:
					isGBetter = gScope <= next.getG()
				if (isGBetter == True):
					next.setStateParent(current)
					next.setG(gScope)
		return 0;
 


	def 	find(self, state, listState, size, sizeLine):
		s = state.getMatrixArray()
		for currentState in listState:
			res = 0
			tmp = currentState.getMatrixArray()
			i = 0
			while (i < sizeLine):
				j = 0
				flagBreak = 0
				while j < sizeLine:
					if (s[i][j] == tmp[i][j]):
						res += 1
					else:
						flagBreak = 1
						break
					j += 1
				i += 1
				if (flagBreak == 1):
					break 
			if (res == size):
				return True
		return (False)

	def 	getStateWithMinF( self, openList ):
		min = sys.maxsize - 1
		i = 0
		i_res = 0
		for state in openList:
			if state.getF() < min:
				min = state.getF()
				i_res = i
			i += 1
		res = copy.deepcopy(openList[i_res])
		return res, i_res

	def 	completeSolution( self, terminate, listState ):
		listState.append(terminate.getMatrixArray())
		if (terminate.countParent != 0):
			return self.completeSolution(terminate.getStateParent(), listState)
		else:
			return listState