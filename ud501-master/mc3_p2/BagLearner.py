"""
import BagLearner as bl
learner = bl.BagLearner(learner = knn.KNNLearner, kwargs = {"k":3}, bags = 20, boost = False, verbose = False)
learner.addEvidence(Xtrain, Ytrain)
Y = learner.query(Xtest)


random with replace
bags == number of bags
each bag should have same size as training set
"""


import numpy as np


class BagLearner(object):

	def __init__(self, learner, kwargs, bags=1, boost=False, verbose=False):
		self.constructor = learner
		self.kwargs = kwargs
		self.bags = bags
		self.boost = boost
		self.verbose = verbose

		# set up a learner for each bag
		self.learners = []
		for i in range(bags):
			self.learners.append(self.constructor(**kwargs))

	def addEvidence(self, dataX, dataY):

		# train each learner with a "random with replacement" dataset
		# A[np.random.randint(10,size=10),:]
		length = dataX.shape[0]
		width = dataX.shape[1] + 1
		merged = np.zeros([length, width])
		merged[:,:-1] = dataX
		merged[:,-1] = dataY

		for i in range(self.bags):
			bagdata = merged[np.random.randint(length,size=length),:]
			bagX = bagdata[:,:-1]
			bagY = bagdata[:,-1]
			self.learners[i].addEvidence(bagX, bagY)

	def query(self, points):

		Y = self.learners[0].query(points)
		if self.bags > 1:
			for i in range(1,self.bags):
				Y += self.learners[i].query(points)
		return Y/self.bags
