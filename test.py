import sys
from object.Matrix import *
import numpy as np
from is_terminate import *
from fcoefficientsearch import *
from read import *
from object.Rules import *
from object.State import *

resultRead = readFile(sys.argv[1])
m = convertInMatrix(resultRead)
sOrigin = State(m)
#print m.matrix


'''
def     search_zero_indices(matryx):
        for i,j in enumerate(matryx):
                for k,l in enumerate(j):
                        if l==0:
				return i,k
'''
#print np.nanargmin(m.matrix, axis=None)

#row,column = search_zero_indices(m.matrix)
#print check_solve(m.matrix)
#print fill_matrix(m.matrix)
#matrix_correct = fill_matrix(m.matrix)
#print m.matrix
#print matrix_correct
#print g_coef_count(matrix_correct, m.matrix)
#digit = 3
rules = Rules(sOrigin)
print "test getH rules =",rules.getH(sOrigin)
print "Need to false =", rules.isTerminate(sOrigin)
print "Need to true =", rules.isTerminate(rules.stateCorrect)
rules.getNeighbors(sOrigin)
# print (rules.getDistance(sOrigin))


'''
m.move_right(row,column)
print m.matrix
row,column = search_zero_indices(m.matrix)
m.move_up(row,column)
print m.matrix
row,column = search_zero_indices(m.matrix)
m.move_left(row,column)
print m.matrix
row,column = search_zero_indices(m.matrix)
m.move_down(row,column)
print m.matrix
'''
