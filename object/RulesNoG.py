from Rules import *

class RulesNoG(Rules):

    def __init__( self, startState):
        Rules.__init__(self, startState)

    def getDistance( self ):
        return (0)
        