import sys
from IHeuristic import *
from Matrix import *
from State import *

class   Manhattan(IHeuristic):

    def getH( self, state, stateCorrect):
        def getIndex( matrix, digit ):
            for row, j in enumerate( matrix ):
                for column,l in enumerate( j ):
                    if l == digit:
                        return ( row, column )
        size = len( state.getMatrixArray( ) )
        max = size * size
        h = 0
        for digit in range( max ):
            indSt = getIndex( state.getMatrixArray(), digit )
            indCor = getIndex( stateCorrect.getMatrixArray(), digit )
            h += abs( indSt[0] - indCor[0] ) + abs( indSt[1] - indCor[1] )
        return (h)
# return ( h + getLinearCoef( self.stateCorrect.getMatrixArray(), state.getMatrixArray() ))