# from abc import ABCMetas

class 	State:

	def __init__(self):
		pass

	def getG(self):
		return self.g;

	def getF(self):
		return self.g + self.h;

	def getH(self):
		return self.h

	def setH(self, h):
		self.h = h;

	def setG(self, g):
		self.g = g;

	def getParent(self):
		return self.parent

	def setParent(self, parent):
		self.parent = parent;