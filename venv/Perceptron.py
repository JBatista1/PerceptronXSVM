from GenerateDataSet import GenereteDataSet
from DataSetManager import DataSetManager
import numpy as np
import random

class Perceptron():

    def __init__(self, xTrain, yTrain, epoch = 100):
        self.__xTrain = xTrain
        self.__ytrain = yTrain
        self.__w = np.zeros(len(xTrain[0]), dtype=float)
        self.__epoch = epoch
        self.__w = self.train(self.__xTrain, self.__ytrain, self.__w)

    def getW(self):
        return self.__w

    def train(self, xTrain, dtrain, w):
        num: int = 0
        while True:
            error = False
            for i in range(len(xTrain)):
                u = self.summationValuesMatrix(xTrain[i], w)
                y = 0
                if u > 0:
                    y = 1
                if y != dtrain[i]:
                    err = dtrain[i] - y
                    for j in range(len(xTrain[i]) - 1):
                        w[j] = w[j] + (err * xTrain[i][j])
                    error = True
            num += 1
            if num > self.__epoch or not error:
                break
        return w

    def validate(self, xValidate, dValidate):
        positive = 0
        arrayRandom = self.__createRandomArray(len(xValidate))
        for index in range(0, len(xValidate)):

            u = self.summationValuesMatrix(xValidate[arrayRandom[index]], self.__w)
            y = 0
            if u <= 0:
                y = 0
            else:
                y = 1
            if y == dValidate[arrayRandom[index]]:
                positive += 1
        return (positive / len(dValidate))


    def summationValuesMatrix(self, x, w):
        valueMultiply = 0
        for i in range(len(x)):
            valueMultiply += x[i] * w[i]
        return valueMultiply

    #Array criado para pegar valores aleatorios dos dados de treinamento
    def __createRandomArray(self, size):
        arrayRandom =[]
        for i in range(size):
            arrayRandom.append(i)
        random.shuffle(arrayRandom)
        return  arrayRandom




dataset = GenereteDataSet(10,10)
xtrain, ytrain = dataset.getDataSetTrain()
xtest, ytest = dataset.getDataSetTest()

# test = DataSetManager(0)
# xtrain ,xtest, ytrain, ytest = test.get_data_X_Y_for_train_and_test()

print(xtrain)

perceptron = Perceptron(xtest, ytest)
acurracy = perceptron.validate(xtrain, ytrain)
print("Acurracy is", acurracy)
# pesos = perceptron.getW()
# func = dataset.getFuncBase()
#
# print(func)
# print(pesos)
