import sys

def 	readFile(nameFile):
	try:
		f = open(nameFile, 'r')
		res = f.read()
		return res.split('\n')
	except:
		print "Read file error."
		sys.exit(1)

resultRead = readFile(sys.argv[1])
for c in resultRead:
	print c