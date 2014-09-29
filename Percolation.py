import QuickUF
import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pylab as pll
class Percolation(object):
	"""docstring for Percolation"""
	def __init__(self, arg):
		super(Percolation, self).__init__()
		self.N = arg
		self.uf = QuickUF.QuickUF(arg*arg)
		self.celda = []
		for i in range(arg+1):
			pass
			self.celda.append([])
			for j in range(arg+1):
				pass
				self.celda[i].append(False)
		for s in range(arg-1):
			pass
			self.uf.unite(self.cell(s,0),self.cell(s+1,0))
			self.uf.unite(self.cell(s,arg-1),self.cell(s+1,arg-1))
		for d in range(arg):
			pass
			self.celda[i][arg-1]=True
			self.celda[i][0]=True
		#print(self.celda)
	def cell(self,i,j):
		return i+j*self.N
	def step(self):
		pass
		i=random.randint(0,self.N-1)
		j=random.randint(0,self.N-1)
		while (self.celda[i][j]):
			i = random.randint(0,self.N-1)
			j = random.randint(0,self.N-1)
		self.celda[i][j] = True
		if ((i < self.N-1)  & self.celda[i+1][j]):
			self.uf.unite(self.cell(i, j), self.cell(i+1, j))
		if (i > 0 & (self.celda[i-1][j])):
			self.uf.unite(self.cell(i,j),self.cell(i-1,j))
		if (j < self.N-1 & self.celda[i][j+1]):
			self.uf.unite(self.cell(i, j), self.cell(i, j+1))
		if (j > 0   & self.celda[i][j-1]):
			self.uf.unite(self.cell(i, j), self.cell(i, j-1))
	def simular(self):
		pass
		i=0
		g = []
		while True:
			pass
			if (self.uf.find(self.cell(0,0),self.cell(self.N-1,self.N-1))):
				plt.plot(g)
				plt.show()
				pll.matshow(self.celda)
				pll.show()
				return int(i)
			i=i+1
			g.append(i/self.N*self.N)
			self.step()