import numpy as np
import random

class Perceptron:
    def __init__(self, xTrain, yTrain):
       self.__xTrain = xTrain
       self.__ytrain = yTrain
       self.__w = np.zeros(len(xTrain), dtype=float)


    def printTeste(self):
        print(self.__w)
        random.shuffle(self.__xTrain)
        print(self.__xTrain)
    def 

perceptron = Perceptron([0,1,2,3],[1,2,3])
perceptron.printTeste()