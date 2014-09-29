class QuickUF(object):
	"""docstring for QuickUF"""
	def __init__(self, arg):
		super(QuickUF, self).__init__()
		self.id = []
		self.componente = arg
		for i in range(arg):
			self.id.append(i)
	def find_(self,x):
		pass
		#print(x)
		while (x!=self.id[x]):
			x = self.id[x]
		return x
	def componente(self):
		pass
		return self.componente
	def find(self,p,q):
		pass
		if(self.find_(p)==self.find_(q)):
			return True
	def unite(self,p,q):
		pass
		i = self.find_(p)
		j = self.find_(q)
		if (i == j):
			pass
			return
		self.id[i]=j
		self.componente = self.componente-1