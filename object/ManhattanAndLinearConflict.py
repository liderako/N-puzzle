import sys
from IHeuristic import *
from Matrix import *
from State import *
from Manhattan import *
import numpy as np
import copy

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

    # def getLinearCoef( self, stateCorrect, stateCurrent ):
    #     dict_right = self.getIndexRightState( stateCorrect )
    #     dict_curr = self.getIndexRightState( stateCurrent )

    #     lst = []
    #     for dig in dict_right:
    #         if dict_curr[dig][0] != dict_right[dig][0] and dict_curr[dig][1] != dict_right[dig][1]:
    #             lst.append(dig)
    #     dict_curr_full = copy.copy(dict_curr)
    #     for i in lst:
    #         dict_curr.pop(i)
    #     size = len(stateCurrent)
    #     row_m = 0
    #     linear_coef = 0
    #     while (row_m < size):
    #         i = -1
    #         while (i >= -size):
    #             digit = int(stateCurrent[row_m][i])
    #             if digit in dict_curr:
    #                 col = i - 1
    #                 while (col >= -size):
    #                     chekd = int(stateCurrent[row_m][col])
    #                     if (dict_right[digit][1] <= dict_right[chekd][1]) and (dict_right[chekd][0] == dict_curr[digit][0]):
    #                         linear_coef += 1
    #                     col -= 1
    #             i -= 1
    #         row_m += 1
    #     return linear_coef

    # def getH( self, state, stateCorrect ):
    #     return ( self.manhattan.getH( state, stateCorrect ) + self.getLinearCoef( stateCorrect.getMatrixArray(), state.getMatrixArray() ) )
    
    # def getSwapCoef( self, stateCorrect, stateCurrent ):
    #     dict_right = self.getIndexRightState( stateCorrect )
    #     dict_curr = self.getIndexRightState( stateCurrent )
    #     lst = []
    #     for dig in dict_right:
    #         if dict_curr[dig][0] != dict_right[dig][0] and dict_curr[dig][1] != dict_right[dig][1]:
    #             lst.append(dig)
    #         elif (abs(dict_curr[dig][0] - dict_right[dig][0]) != 1 and dict_curr[dig][1] - dict_right[dig][1] == 0) or (dict_curr[dig][0] - dict_right[dig][0] == 0 and abs(dict_curr[dig][1] - dict_right[dig][1]) != 1):
    #             lst.append(dig)
    #     for i in lst:
    #         dict_curr.pop(i)
    #         dict_right.pop(i)
    #     # print dict_curr
    #     # print dict_right
    #     lst = []
    #     for dig in dict_curr:
    #         row = dict_curr[dig][0]
    #         col = dict_curr[dig][1]
    #         flag = 0
    #         for i in dict_right:
    #             if row == dict_right[i][0] and col == dict_right[i][1]:
    #                 flag = 1
    #         if flag == 0:
    #             lst.append(dig)
    #     for i in lst:
    #         dict_curr.pop(i)
    #     return len(dict_curr)

    def getTilesOutCoef( self, stateCorrect, stateCurrent ):
        dict_right = self.getIndexRightState( stateCorrect )
        dict_curr = self.getIndexRightState( stateCurrent )
        tcoef = 0
        for dig in dict_right:
            if dict_curr[dig][0] != dict_right[dig][0]:
                tcoef += 1
            if dict_curr[dig][1] != dict_right[dig][1]:
                tcoef += 1
        return tcoef

    def getH( self, state, stateCorrect ):
        return (self.getTilesOutCoef(stateCorrect.getMatrixArray(), state.getMatrixArray()))

    # def getH( self, state, stateCorrect ):
        # return (self.getSwapCoef(stateCorrect.getMatrixArray(), state.getMatrixArray() ))