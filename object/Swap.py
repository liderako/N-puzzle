import sys
from Heuristic import *
from Matrix import *
from State import *
from Manhattan import *
import numpy as np
import copy

class   Swap(Heuristic):

    def getSwapCoef( self, stateCorrect, stateCurrent ):
        dictRight = self.getIndexRightState( stateCorrect )
        dictCurr = self.getIndexRightState( stateCurrent )
        lst = []
        for dig in dictRight:
            if dictCurr[dig][0] != dictRight[dig][0] and dictCurr[dig][1] != dictRight[dig][1]:
                lst.append(dig)
            elif (abs(dictCurr[dig][0] - dictRight[dig][0]) != 1 and dictCurr[dig][1] - dictRight[dig][1] == 0) or (dictCurr[dig][0] - dictRight[dig][0] == 0 and abs(dictCurr[dig][1] - dictRight[dig][1]) != 1):
                lst.append(dig)
        for i in lst:
            dictCurr.pop(i)
            dictRight.pop(i)
        lst = []
        for dig in dictCurr:
            row = dictCurr[dig][0]
            col = dictCurr[dig][1]
            flag = 0
            for i in dictRight:
                if row == dictRight[i][0] and col == dictRight[i][1]:
                    flag = 1
            if flag == 0:
                lst.append(dig)
        for i in lst:
            dictCurr.pop(i)
        return len(dictCurr)

    def getH( self, state, stateCorrect ):
        return ( self.getSwapCoef( stateCorrect.getMatrixArray(), state.getMatrixArray() ))