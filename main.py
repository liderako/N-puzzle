import hashlib
import sys
from object.Matrix import *
import numpy as np
from is_terminate import *
from fcoefficientsearch import *
from read import *
from object.Rules import *
from object.RulesG import *
from object.RulesNoG import *
from object.State import *
from object.Astar import *

if (len(sys.argv) != 3):
	print "Usage python main.py maps/anyoneMaps [-g=true or -g=false]"
	sys.exit(1)
if (sys.argv[2] != "-g=true" and sys.argv[2] != "-g=false"):
	print "Usage python main.py maps/anyoneMaps [-g=true or -g=false]"
	sys.exit(1)

resultRead = readFile(sys.argv[1])
m = convertInMatrix(resultRead)
sOrigin = State(m)

if (sys.argv[2] == "-g=false"):
	rules = RulesNoG(sOrigin)
else:
	rules = RulesG(sOrigin)

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