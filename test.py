import sys
from object.Matrix import *
import numpy as np
from is_terminate import *
from fcoefficientsearch import *
from read import *
from object.Rules import *
from object.State import *
from object.Astar import *

resultRead = readFile(sys.argv[1])
m = convertInMatrix(resultRead)
sOrigin = State(m)

rules = Rules(sOrigin)
astar = Astar(rules)

a = astar.search(sOrigin)
print a
# test = rules.getNeighbors(sOrigin)
# for x in test:
# 	print x.getMatrixArray()
# 	print "\n"
# test = search()

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
