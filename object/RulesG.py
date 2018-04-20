from Rules import *

class RulesG(Rules):

    def __init__( self, startState, heuristic):
        Rules.__init__(self, startState, heuristic)

    def getDistance( self ):
        return (1)