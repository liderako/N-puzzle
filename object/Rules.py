class 	Rules:

	def 	__init__( self ):
		pass
###
	def getNeighbors( self, currentState ):
		print "State getHeighbors"
		# @return the list of states in which the transition from specified state.

	# Returns the distance between the specified states.
	def getDistance( self, stateStart, stateEnd ):
		def gCoefCount( matrixStart, matrixEnd ):
    		gCoef = 0    
			for i,j in enumerate( matrixStart ):
                for k,l in enumerate( j ):
                        if matrixStart[i][k] != matrixEnd[i][k]:
                            gCoef += 1
            return gCoef
        return gCoefCount( stateStart.matrix, stateEnd.matrix)

	 # Calculates a heuristic estimate of the distance from the specified state to the final.
	def getH( self, state ):
		def get_index(matrix, digit):
			for row,j in enumerate(matrix):
				for column,l in enumerate(j):
					if l == digit:
						return row, column
		indSt =  get_index(state, digit)
		indCor = get_index(correctState, digit)
		h = abs(indSt[0] - indCor[0]) + abs(indSt[1] -indCor[1])
		return h

	# Checks whether the state is finished.
	def isTerminate( self, state ):
		return False;
