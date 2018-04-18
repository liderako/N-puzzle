import sys
import copy
from State import *
from fcoefficientsearch import *
from linearconflict import *
from is_terminate import *
from IRules import *

class   Rules(IRules):
    def __init__( self, startState):
        m = Matrix( startState.matrix.size )
        m.setMatrix( fill_matrix( startState.getMatrixArray() ))
        self.stateCorrect = State( m )
        self.stateCorrect.mathHash()

    def copyState( self, stateCurrent, indZero, key ):
        a = State( copy.deepcopy( stateCurrent.getMatrixObject() ))
        if ( key == "right" ):
            a.getMatrixObject().moveRight( indZero[0], indZero[1] )
        elif (key == "down" ):
            a.getMatrixObject().moveDown( indZero[0], indZero[1] )
        elif ( key == "up" ):
            a.getMatrixObject().moveUp( indZero[0], indZero[1] )
        elif ( key == "left" ):
            a.getMatrixObject().moveLeft( indZero[0], indZero[1] )
        return ( a )

    def getNeighbors( self, stateCurrent ):
        stateList = list( )
        def getIndexzero( matrix ):
            for row, j in enumerate( matrix ):
                for column,l in enumerate( j ):
                    if l == 0:
                        return ( row, column )
        sz = stateCurrent.matrix.size - 1
        indZero = getIndexzero( stateCurrent.getMatrixArray( ) )
        if ( 0 < indZero[0] < sz ) and ( 0 < indZero[1] < sz ):
            stateList.append( self.copyState( stateCurrent, indZero, "right" ))
            stateList.append( self.copyState( stateCurrent, indZero, "left" ))
            stateList.append( self.copyState( stateCurrent, indZero, "down" ))
            stateList.append( self.copyState( stateCurrent, indZero, "up" ))
# # at left column
        elif ( 0 < indZero[0] < sz ) and ( indZero[1] == 0 ):
            stateList.append( self.copyState( stateCurrent, indZero, "right" ))
            stateList.append( self.copyState( stateCurrent, indZero, "down" ))
            stateList.append( self.copyState( stateCurrent, indZero, "up" ))
# # at right column
        elif ( 0 < indZero[0] < sz ) and ( indZero[1] == sz ):
            stateList.append( self.copyState(stateCurrent, indZero, "left" ) )
            stateList.append( self.copyState(stateCurrent, indZero, "down" ) )
            stateList.append( self.copyState(stateCurrent, indZero, "up" ) )
# # at top row
        elif ( indZero[0] == 0 ) and ( 0 < indZero[1] < sz ):
            stateList.append( self.copyState(stateCurrent, indZero, "right" ) )
            stateList.append( self.copyState(stateCurrent, indZero, "left" ) )
            stateList.append( self.copyState(stateCurrent, indZero, "down" ) )
# # at down row
        elif ( indZero[0] == sz ) and ( 0 < indZero[1] < sz ):
            stateList.append( self.copyState(stateCurrent, indZero, "right" ) )
            stateList.append( self.copyState( stateCurrent, indZero, "left" ) )
            stateList.append( self.copyState( stateCurrent, indZero, "up" ) )
# # at left top corner
        elif ( indZero[0] == 0 ) and ( indZero[1] == 0 ):
            stateList.append( self.copyState( stateCurrent, indZero, "right" ) )
            stateList.append( self.copyState( stateCurrent, indZero, "down" ) )
# # at right top corner
        elif ( indZero[0] == 0 ) and (indZero[1] == sz ):
            stateList.append( self.copyState( stateCurrent, indZero, "left" ) )
            stateList.append( self.copyState( stateCurrent, indZero, "down" ) )
# # at left down corner
        elif ( indZero[0] == sz ) and (indZero[1] == 0 ):
            stateList.append( self.copyState( stateCurrent, indZero, "right" ) )
            stateList.append( self.copyState( stateCurrent, indZero, "up" ) )
# # at right down corner
        elif ( indZero[0] == sz ) and ( indZero[1] == sz ):
            stateList.append( self.copyState( stateCurrent, indZero, "up" ) )
            stateList.append( self.copyState( stateCurrent, indZero, "left" ) )
        return ( stateList )

    def getH( self, state ):
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
            indCor = getIndex( self.stateCorrect.getMatrixArray(), digit )
            h += abs( indSt[0] - indCor[0] ) + abs( indSt[1] - indCor[1] )
            # print getLinearCoef( self.stateCorrect.getMatrixArray(), state.getMatrixArray() )
        # return ( h + getLinearCoef( self.stateCorrect.getMatrixArray(), state.getMatrixArray() ))
        return (h)
    def isTerminate( self, state ):
        return ( self.find( state, self.stateCorrect ))

    def     find( self, state, stateCorrect ):
        if ( state == stateCorrect ):
            return ( True )
        return ( False )