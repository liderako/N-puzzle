class A:
	def __init__(self):
		self.name = "anton"
		self.age = 18
	def getName(self):
		return (self.name)

class B(A):
	def __init__(self):
		# self.name = "toxa"
		A.__init__(self)
		self.name = "toxa2"
		# super(B, self).__init__()

# class ClassName(object):
# 	"""docstring for ClassName"""
# 	def __init__(self, arg):
# 		super(ClassName, self).__init__()
# 		self.arg = arg
		

b = B()

print b.getName()