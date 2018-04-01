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
        stateList = list()
        stateList1 = list()
        def getIndexzero( matrix ):
            for row, j in enumerate( matrix ):
                for column,l in enumerate( j ):
                    if l == 0:
                        return row, column
        # for exemple
        i  = 0
        while i < 3:
            mObject = Matrix(10)
            stateObject = State(mObject)
            #print stateObject.getMatrixArray(), "\n"
            stateList1.append( stateObject )
            i += 1
        ## end exemple
        sz = stateCurrent.matrix.size - 1
#        print stateCurrent.getMatrixArray()
        indZero = getIndexzero( stateCurrent.getMatrixArray() )
        print indZero
        arr = Matrix( stateCurrent.matrix.size )
        matr = State( arr )
#        matr = State( stateCurrent.getMatrixArray() )
        print matr.getMatrixArray()
#        matr[4][1] = 3
        #matr = stateCurrent.getMatrixArray()[:]
        print "NewMatr"
        print matr.getMatrixArray()
        
        return stateList

#        new_matrix = 
#        print arr.getMatrixArray()
        if (0 < indZero[0] < sz) and (0 < indZero[1] < sz):
            stateList.append( new_matrix.move_right(indZero[0], indZero[1]) )
            stateList.append( new_matrix.move_left(indZero[0], indZero[1]) )
            stateList.append( new_matrix.move_up(indZero[0], indZero[1]) )
            stateList.append( new_matrix.move_down(indZero[0], indZero[1]) )
# at left column
        elif (0 < indZero[0] < sz) and (indZero[1] == 0):
            stateList.append( new_matrix.move_right(indZero[0], indZero[1]) )
            stateList.append( new_matrix.move_up(indZero[0], indZero[1]) )
            stateList.append( new_matrix.move_down(indZero[0], indZero[1]) )
# at right column
        elif (0 < indZero[0] < sz) and (indZero[1] == sz):
            stateList.append( new_matrix.move_left(indZero[0], indZero[1]) )
            stateList.append( new_matrix.move_up(indZero[0], indZero[1]) )
            stateList.append( new_matrix.move_down(indZero[0], indZero[1]) )
# at top row
        elif (indZero[0] == 0) and (0 < indZero[1] < sz):
            stateList.append( new_matrix.move_right(indZero[0], indZero[1]) )
            stateList.append( new_matrix.move_left(indZero[0], indZero[1]) )
            stateList.append( new_matrix.move_down(indZero[0], indZero[1]) )
# at down row
        elif (indZero[0] == sz) and (0 < indZero[1] < sz):
            stateList.append( new_matrix.move_right(indZero[0], indZero[1]) )
            stateList.append( new_matrix.move_left(indZero[0], indZero[1]) )
            stateList.append( new_matrix.move_up(indZero[0], indZero[1]) )
# at left top corner
        elif (indZero[0] == 0) and (indZero[1] == 0):
            stateList.append( new_matrix.move_right(indZero[0], indZero[1]) )
            stateList.append( new_matrix.move_down(indZero[0], indZero[1]) )
# at right top corner
        elif (indZero[0] == 0) and (indZero[1] == sz):
            stateList.append( new_matrix.move_left(indZero[0], indZero[1]) )
            stateList.append( new_matrix.move_down(indZero[0], indZero[1]) )
# at left down corner
        elif (indZero[0] == sz) and (indZero[1] == 0):
            stateList.append( new_matrix.move_right(indZero[0], indZero[1]) )
            stateList.append( new_matrix.move_up(indZero[0], indZero[1]) )
# at right down corner
        elif (indZero[0] == sz) and (indZero[1] == sz):
            stateList.append( new_matrix.move_up(indZero[0], indZero[1]) )
            stateList.append( new_matrix.move_left(indZero[0], indZero[1]) )
        return stateList

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
