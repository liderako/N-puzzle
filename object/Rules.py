import sys
from State import *
from fcoefficientsearch import *
from is_terminate import *

class 	Rules:
    def __init__( self, startState ):
        m = Matrix( startState.matrix.size )
        m.setMatrix( fill_matrix( startState.getMatrixArray() ) )
        self.stateCorrect = State( m )

    def getNeighbors( self, stateCurrent ):
        print "State getHeighbors"
        # @return the list of states in which the transition from specified state.

    # Returns the distance between the specified states.
    def getDistance( self, stateStart, stateEnd=0 ):
        if stateEnd == 0:
            stateEnd = self.stateCorrect
        def gCoefCount( matrixStart, matrixEnd ):
            gCoef = 0    
            for i,j in enumerate( matrixStart ):
                for k,l in enumerate( j ):
                    if matrixStart[i][k] != matrixEnd[i][k]:
                        gCoef += 1
            return gCoef
        return gCoefCount( stateStart.getMatrixArray(), stateEnd.getMatrixArray() )

    # Calculates a heuristic estimate of the distance from the specified state to the final.
    def getH( self, state ):
        def getIndex( matrix, digit ):
            for row, j in enumerate( matrix ):
                for column,l in enumerate( j ):
                    if l == digit:
                        return row, column
        size = len( state.getMatrixArray() )
        max = size * size
        h = 0
        for digit in range( max ):
            indSt = getIndex( state.getMatrixArray(), digit )
            indCor = getIndex( self.stateCorrect.getMatrixArray(), digit )
            h += abs( indSt[0] - indCor[0] ) + abs( indSt[1] - indCor[1] )
        return h
    
    # Checks whether the state is finished.
    def isTerminate( self, state ):
        return check_solve( state.getMatrixArray() );
