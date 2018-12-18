import pandas as pd
import numpy as np

# import ml algorithms
from sklearn.linear_model import LogisticRegression
from sklearn import svm


class MachineLearningClassifier(object):
    """ Train ML classifier in this class"""
    @staticmethod
    def svm_classifier(x, y):
        x= np.array(x).reshape(-1,1)
        y = np.array(y)
        """ svm classifier """
        svmClassifier = svm.SVC(kernel='rbf')
        svmClassifier.fit(x, y)
        return svmClassifier

    @staticmethod
    def logistic_regression_classifier(x, y):
        """ LR classifier"""
        x= np.array(x).reshape(-1,1)
        y = np.array(y)

        print("X :",x)
        print("Y : ", y)
        logistic = LogisticRegression()
        logistic.fit(x, y)
        return logistic

    
