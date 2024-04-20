import numpy as np


class Perceptron:
    def __init__(self):
        self.weights_ = None

    def fit(self, x, y):
        self.weights_ = np.zeros(x.shape[1])
        for i in range(0,100):
            i=0
            for gt in y:
                pred= self.predict(x.iloc[i, :])
                if (pred < gt):
                    self.weights_ = np.add(self.weights_, x.iloc[i,:])
                if (pred > gt):
                    self.weights_ = np.subtract(self.weights_, x.iloc[i, :])
                i+=1

    def predict(self, x):
        calc = np.dot(x, np.transpose(self.weights_))
        return -1 if calc < 0 else 1

    def score(self,x,y):
        count_true =0
        i=0
        for gt in y:
            pred = self.predict(x.iloc[i, :])
            if pred == gt:
                count_true+=1
            i+=1
        return count_true/y.shape[0]








