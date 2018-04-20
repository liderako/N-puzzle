import sys
from IHeuristic import *
from Matrix import *
from State import *
from Manhattan import *
import numpy as np

class   ManhattanAndLinearConflict(IHeuristic):

    def __init__( self, manhattan ):
        self.manhattan = manhattan

    def getIndexRightState( self, state ):
        def getIndex( matrix, digit ):
            for row, j in enumerate( matrix ):
                    for column,l in enumerate( j ):
                        if l == digit:
                           return row, column
        dict = {}
        for row, j in enumerate( state ):
            for column,l in enumerate( j ):
                list = getIndex(state, l)
                dict.update({int(l): list})
        return dict

    def getLinearCoef( self, stateCorrect, stateCurrent):
        dict_right = self.getIndexRightState( stateCorrect )
        dict_curr = self.getIndexRightState( stateCurrent )
        lst = []
        for dig in dict_right:
            if dict_curr[dig][0] != dict_right[dig][0] and dict_curr[dig][1] != dict_right[dig][1]:
                lst.append(dig)
            elif (abs(dict_curr[dig][0] - dict_right[dig][0]) != 1 and dict_curr[dig][1] - dict_right[dig][1] == 0) or (dict_curr[dig][0] - dict_right[dig][0] == 0 and abs(dict_curr[dig][1] - dict_right[dig][1]) != 1):
                lst.append(dig)
        for i in lst:
            dict_curr.pop(i)
            dict_right.pop(i)
        return len(dict_curr)

    def getH( self, state, stateCorrect ):
        return ( self.manhattan.getH( state, stateCorrect ) + self.getLinearCoef( stateCorrect.getMatrixArray(), state.getMatrixArray() ) )
