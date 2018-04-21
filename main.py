import hashlib
import sys
from object.Matrix import *
import numpy as np
from is_terminate import *
from fcoefficientsearch import *
from read import *
from object.Rules import *
from object.State import *
from object.Astar import *
from object.Manhattan import *
from object.ManhattanAndLinearConflict import *
from object.Misplaced import *
from object.Swap import *
from object.TilesOut import *

stringUsage = "Usage python main.py maps/anyoneMaps [-g=true or -g=false] [-m or -ml or -mi]"

if (len(sys.argv) != 4):
	print stringUsage
	sys.exit(1)
if (sys.argv[2] != "-g=true" and sys.argv[2] != "-g=false"):
	print stringUsage
	sys.exit(1)
if (sys.argv[3] != "-m" and sys.argv[3] != '-ml' and sys.argv[3] != "-mi" and sys.argv[3] != "-to" and sys.argv[3] != "-swap"):
	print stringUsage
	sys.exit(1)

resultRead = readFile(sys.argv[1])
m = convertInMatrix(resultRead)
sOrigin = State(m)

if (sys.argv[3] == "-m"):
	heuristic = Manhattan()
elif (sys.argv[3] == "-ml"):
	heuristic = ManhattanAndLinearConflict(Manhattan())
elif (sys.argv[3] == "-mi"):
	heuristic = Misplaced()
elif (sys.argv[3] == "-to"):
	heuristic = TilesOut(Manhattan())
elif (sys.argv[3] == "-swap"):
	heuristic = Swap()

if (sys.argv[2] == "-g=false"):
	rules = Rules(sOrigin, heuristic, 0)
else:
	rules = Rules(sOrigin, heuristic, 1)

astar = Astar(rules)

a = astar.search(sOrigin)
size = len(a)
print "Steps"
i = size - 1
step = 1
while i > 0:
	print "step ", step, "\n", a[i]
	i -=1
	step += 1
print "Solution\n", a[0]
print "Total number of states: ",astar.totalSizeState
print "Max number of states: ", astar.totalMaxSizeState  
print "Count step move", size - 1