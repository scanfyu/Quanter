"""
Test a learner.  (c) 2015 Tucker Balch
"""

from matplotlib import pyplot as plt

import numpy as np
import math
import LinRegLearner as lrl
import KNNLearner as knn 
import BagLearner as bl 


if __name__=="__main__":
    inf = open('Data/ripple.csv')
    data = np.array([list(map(float,s.strip().split(','))) for s in inf.readlines()])

    # compute how much of the data is training and testing
    train_rows = int(math.floor(0.6* data.shape[0]))
    test_rows = int(data.shape[0] - train_rows)

    # separate out training and testing data
    trainX = data[:train_rows,0:-1]
    trainY = data[:train_rows,-1]
    testX = data[train_rows:,0:-1]
    testY = data[train_rows:,-1]

    def analyse(learner, trainX, trainY, testX, testY, description):
        learner.addEvidence(trainX, trainY)
        predY = learner.query(trainX)

        rmse = math.sqrt(((trainY - predY) ** 2).sum()/trainY.shape[0])
        c = np.corrcoef(predY, y=trainY)

        fig = plt.figure()
        plt.scatter(trainY, predY)
        title = description + " rmse " + str(rmse) + " c " + str(c[0,1])
        fig.suptitle(title, fontsize=16)
        plt.xlabel('Input')
        plt.ylabel('Output')
        plt.savefig(description.strip() + ".png", bbox_inches='tight')
        plt.show()


    #learner1 = bl.BagLearner(learner = lrl.LinRegLearner, kwargs = {k:1}, bags = 20, boost = False, verbose = False)
    #analyse(learner1, trainX, trainY, testX, testY, "BagLearner: 20 KNNLearner k=1")

    learner2 = knn.KNNLearner(k=300)
    analyse(learner2, trainX, trainY, testX, testY, "KNNLearner k=3 white_wine OutOfSample")

"""
    knn_oo_s4 = knn.KNNLearner(k=4, verbose=False)
    analyse(knn_oo_s4, trainX, trainY, testX, testY, "KNNLearner k=4 OutOfSample")

    knn_in_s4 = knn.KNNLearner(k=4, verbose=False)
    analyse(knn_in_s4, trainX, trainY, trainX, trainY, "KNNLearner k=4 InSample")

    knn_oo_s1 = knn.KNNLearner(k=5, verbose=False)
    analyse(knn_oo_s1, trainX, trainY, testX, testY, "KNNLearner k=5 OutOfSample")

    knn_in_s1 = knn.KNNLearner(k=5, verbose=False)
    analyse(knn_in_s1, trainX, trainY, trainX, trainY, "KNNLearner k=5 InSample")

    knn_oo_s1 = knn.KNNLearner(k=1, verbose=False)
    analyse(knn_oo_s1, trainX, trainY, testX, testY, "KNNLearner k=1 OutOfSample")

    knn_in_s1 = knn.KNNLearner(k=1, verbose=False)
    analyse(knn_in_s1, trainX, trainY, trainX, trainY, "KNNLearner k=1 InSample")

    knn_in_s2 = knn.KNNLearner(k=2, verbose=False)
    analyse(knn_in_s2, trainX, trainY, trainX, trainY, "KNNLearner k=2 InSample")

    knn_in_s3 = knn.KNNLearner(k=3, verbose=False)
    analyse(knn_in_s3, trainX, trainY, trainX, trainY, "KNNLearner k=3 InSample")

    knn_oo_s2 = knn.KNNLearner(k=2, verbose=False)
    analyse(knn_oo_s2, trainX, trainY, testX, testY, "KNNLearner k=2 OutOfSample")

    knn_oo_s3 = knn.KNNLearner(k=3, verbose=False)
    analyse(knn_oo_s3, trainX, trainY, testX, testY, "KNNLearner k=3 OutOfSample")

    lrl_in_s = lrl.LinRegLearner(verbose=False)
    analyse(lrl_in_s, trainX, trainY, trainX, trainY, "LinRegLearner InSample")

    lrl_oo_s = lrl.LinRegLearner(verbose=False)
    analyse(lrl_oo_s, trainX, trainY, testX, testY, "LinRegLearner OutOfSample")
"""
    #learners = []
    #for i in range(0,10):
        #kwargs = {"k":i}
        #learners.append(lrl.LinRegLearner(**kwargs))
