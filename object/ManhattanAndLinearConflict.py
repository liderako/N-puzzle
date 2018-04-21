import sys
from Heuristic import *
from Matrix import *
from State import *
from Manhattan import *
import numpy as np
import copy

class   ManhattanAndLinearConflict(Heuristic):

    def __init__( self, manhattan ):
        self.manhattan = manhattan

    def getLinearCoef( self, stateCorrect, stateCurrent ):
        dict_right = self.getIndexRightState( stateCorrect )
        dict_curr = self.getIndexRightState( stateCurrent )

        lst = []
        for dig in dict_right:
            if dict_curr[dig][0] != dict_right[dig][0] and dict_curr[dig][1] != dict_right[dig][1]:
                lst.append(dig)
        dict_curr_full = copy.copy(dict_curr)
        for i in lst:
            dict_curr.pop(i)
        size = len(stateCurrent)
        row_m = 0
        linear_coef = 0
        while (row_m < size):
            i = -1
            while (i >= -size):
                digit = int(stateCurrent[row_m][i])
                if digit in dict_curr:
                    col = i - 1
                    while (col >= -size):
                        chekd = int(stateCurrent[row_m][col])
                        if (dict_right[digit][1] <= dict_right[chekd][1]) and (dict_right[chekd][0] == dict_curr[digit][0]):
                            linear_coef += 1
                        col -= 1
                i -= 1
            row_m += 1
        return linear_coef
    def getH( self, state, stateCorrect ):
        return ( self.manhattan.getH( state, stateCorrect ) + self.getLinearCoef( stateCorrect.getMatrixArray(), state.getMatrixArray() ) )