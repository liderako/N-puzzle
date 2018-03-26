class 	Rules:

	def 	__init__( self ):
		pass
###
	def getNeighbors( self, currentState ):
		print "State getHeighbors"
		# @return the list of states in which the transition from specified state.
	
	# Returns the distance between the specified states.
	def getDistance( self, stateA, stateB ):
		print "State getDistance"

	#  Calculates a heuristic estimate of the distance from the specified state to the final.
	def getH( self, state, correct_state, digit ):
		def get_index(matrix, digit):
			for row,j in enumerate(matrix):
				for column,l in enumerate(j):
					if l==digit:
						return row, column
		ind_st =  get_index(state, digit)
		ind_cor = get_index(correct_state, digit)
		h = abs(ind_st[0] - ind_cor[0]) + abs(ind_st[1] -ind_cor[1])
		return h

	# Checks whether the state is finished.
	def isTerminate( self, state ):
		return False;
