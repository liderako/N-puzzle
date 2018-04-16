import sys
import copy
from State import *
from fcoefficientsearch import *
from is_terminate import *

class   Rules:
    def __init__( self, startState ):
        m = Matrix( startState.matrix.size )
        m.setMatrix( fill_matrix( startState.getMatrixArray() ) )
        self.stateCorrect = State( m )

    def copyState(self, stateCurrent, indZero, key):
        a = State(stateCurrent.getMatrixObject())
        if (key == "right"):
            a.getMatrixObject().move_right(indZero[0], indZero[1])
        elif key == "down":
            a.getMatrixObject().move_down(indZero[0], indZero[1])
        elif key == "up":
            a.getMatrixObject().move_up(indZero[0], indZero[1])
        elif key == "left":
            a.getMatrixObject().move_left(indZero[0], indZero[1])
        return a

    def getNeighbors( self, stateCurrent ):
        stateList = list()

        def getIndexzero( matrix ):
            for row, j in enumerate( matrix ):
                for column,l in enumerate( j ):
                    if l == 0:
                        return row, column
        sz = stateCurrent.matrix.size - 1
        indZero = getIndexzero(stateCurrent.getMatrixArray())
        if (0 < indZero[0] < sz) and (0 < indZero[1] < sz):
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "right"))
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "left"))
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "down"))
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "up"))
# at left column
        elif (0 < indZero[0] < sz) and (indZero[1] == 0):
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "right"))
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "down"))
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "up"))
# # at right column
        elif (0 < indZero[0] < sz) and (indZero[1] == sz):
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "left"))
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "down"))
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "up"))
# # at top row
        elif (indZero[0] == 0) and (0 < indZero[1] < sz):
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "right"))
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "left"))
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "down"))
# # at down row
        elif (indZero[0] == sz) and (0 < indZero[1] < sz):
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "right"))
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "left"))
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "up"))
# # at left top corner
        elif (indZero[0] == 0) and (indZero[1] == 0):
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "right"))
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "down"))
# # at right top corner
        elif (indZero[0] == 0) and (indZero[1] == sz):
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "left"))
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "down"))
# # at left down corner
        elif (indZero[0] == sz) and (indZero[1] == 0):
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "right"))
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "up"))
# # at right down corner
        elif (indZero[0] == sz) and (indZero[1] == sz):
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "up"))
            stateList.append(self.copyState(copy.deepcopy(stateCurrent), indZero, "left"))
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

    def isTerminate( self, state ):
        return self.find(state, self.stateCorrect)

    def     find(self, state, stateCorrect):
        res = 0
        sizeLine = state.getMatrixObject().getSize()
        size = sizeLine * sizeLine
        s = state.getMatrixArray()
        tmp = stateCorrect.getMatrixArray()
        i = 0
        while (i < sizeLine):
            j = 0
            while j < sizeLine:
                if (s[i][j] != tmp[i][j]):
                    return False
                j += 1
            i += 1
        return (True)