from abc import ABCMetas

class IRules:

	#  Returns a list of states that can be migrated from the status field.
	#  @param currentState - The current state for which the neighboring are revealed
	@abstractmethod
	def getHeighbors( self, currentState ):
		pass
		# @return the list of states in which the transition from specified state.
	
	# Returns the distance between the specified states.
	@abstractmethod
	def getDistance( self, stateA, stateB ):
		pass

	#  Calculates a heuristic estimate of the distance from the specified state to the final.
	@abstractmethod
	def getH( state ):
		pass

	# Checks whether the state is finite.
	@abstractmethod
	def isTerminate( state ):
		# return bool
		pass
