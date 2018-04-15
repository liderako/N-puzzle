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

# a = State(Matrix(3))

# listState = list()

# listState.append(a)

# a.setH(10)

# for x in listState:
# 	print x.getH()