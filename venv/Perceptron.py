import numpy as np
import random

class Perceptron:

    def __init__(self, xTrain, yTrain, epoch = 100):
        self.__xTrain = xTrain
        self.__ytrain = yTrain
        self.__w = np.zeros(len(xTrain), dtype=float)
        self.__epoch = epoch


    # def __train(self):



    def multiplyMatrix(self, matrix1, matrix2):
        traspose = np.transpose(matrix1)
        result = np.dot(matrix1, matrix2)
        print(result)

    #Array criado para pegar valores aleatorios dos dados de treinamento
    def __createRandomArray(self, size):
        arrayRandom =[]
        for i in range(size):
            arrayRandom.append(i)
        random.shuffle(arrayRandom)
        return  arrayRandom


    def printTeste(self):
        print(self.__w)
        print(self.__xTrain)




perceptron = Perceptron([[-1,3],[4,2]],[[1,2],[3,4]])
perceptron.multiplyMatrix([-1,3,3],[1, 3,4])