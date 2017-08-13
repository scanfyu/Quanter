
"""
TODO: implement the following API:

import KNNLearner as knn
learner = knn.KNNLearner(k = 3, verbose = False) # constructor
learner.addEvidence(sample, Ytrain) # training step
Y = learner.query(Xtest) # query

Where "k" is the number of nearest neighbors to find. sample and Xtest should be ndarrays (numpy objects) 
where each row represents an X1, X2, X3... XN set of feature values. The columns are the features 
and the rows are the individual example instances. Y and Ytrain are single dimension ndarrays 
that indicate the value we are attempting to predict with X.

If "verbose" is True, your code can print out information for debugging. Otherwise your code should 
not generate ANY output.

Use Euclidean distance. Take the mean of the closest k points' Y values to make your prediction. 
If there are multiple equidistant points on the boundary of being selected or not selected, 
you may use whatever method you like to choose among them.

This code should not generate statistics or charts. Modify testlearner.py to generate statistics and charts. 
"""

import numpy as np

class KNNLearner(object):

	def __init__(self, k=3, verbose=False):
		self.k = k
		self.verbose = verbose
		self.sample = None

	def addEvidence(self, Xtrain, Ytrain):
		"""
        @summary: Add training data to learner
        @param dataX: X values of data to add
        @param dataY: the Y training values
        """
		#if not isinstance(self.sample, np.ndarray):
		self.sample = np.zeros((Xtrain.shape[0], Xtrain.shape[1]+2))
		self.sample[:,0:-2] = Xtrain
		self.sample[:,-2] = Ytrain
		#else:
		#	concat = np.zeros((Xtrain.shape[0], Xtrain.shape[1]+2))
		#	concat[:,0:-2] = Xtrain
		#	concat[:,-2] = Ytrain
		#	self.sample = np.concatenate((self.sample, concat))

	def query(self, Xtest):
		"""
		@summary: Get perdicted Y values
		@param Xtest: X values
		@returns the estimated values according to the saved model
		"""
		Y = np.zeros((Xtest.shape[0],))

		for i in range(Xtest.shape[0]):
			self.sample[:,-1] = np.sqrt(np.sum((self.sample[:,:-2] - Xtest[i,:])**2, axis=1))
			self.sample = self.sample[self.sample[:,-1].argsort()]
			Y[i] = np.mean(self.sample[:self.k,-2])

		return Y