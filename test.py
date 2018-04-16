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

# m1 = Matrix(3)
# m3 =/ Matrix(3)
# m2 = sOrigin.getMatrixObject()
# 
# if m1.getMatrix() in m2.getMatrix()) == True:
	# print m1.getMatrix()
	# print m2.getMatrix()

a = astar.search(sOrigin)
size = len(a)
print "Count step", size
print "Solution\n", a[0]
print "Steps"

i = size - 1
step = 1
while i >= 0:
	print "step ", step, "\n", a[i]
	i -=1
	step += 1
# for x in a:
	# print x

# a = State(Matrix(3))

# listState = list()

# listState.append(a)

# a.setH(10)

# for x in listState:
# 	print x.getH()