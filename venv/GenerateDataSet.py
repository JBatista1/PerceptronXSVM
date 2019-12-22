import numpy as np
import random

class GenereteDataSet:
    def __init__(self, sizeTrain, sizeTest):
        self.__funcTarget = []
        self.__pointsFunc = []
        self.__sizeTrain = sizeTrain
        self.__sizeTest = sizeTest

        self.__createBasePoints(2)
        self.__createFunc()

    def getDataSetTrain(self):
        run = True
        while(run):
            x, y = self.__createDataSet(self.__sizeTrain)
            verify = self.__checkDistribution(y)
            if verify == run:
                run = False
        return x, y

    def getDataSetTest(self):
        x, y = self.__createDataSet(self.__sizeTest)
        return x, y

    def getFuncBase(self):
        return self.__funcTarget

    def __createBasePoints(self, numberPoints):
        for i in range(numberPoints):
            x0 = self.__generateValueBetween()
            x1 = self.__generateValueBetween()
            self.__pointsFunc.append([x0, x1])

    # Baseado no coeficiente angular da reta obtemos a seguinte equiacao:
    # mx + m(-x0) + y0 = y
    # Onde m é o coeficiente angular, x0 e y0 são os valores de um ponto a qual usamos para criar a equiacao, neste caso e o primeiro ponto
    def __createFunc(self):
        angularCoefficient = (self.__pointsFunc[0][1] - self.__pointsFunc[1][1]) / (self.__pointsFunc[0][0] - self.__pointsFunc[1][0])
        constan = angularCoefficient * (- self.__pointsFunc[0][0]) + self.__pointsFunc[0][1]
        self.__funcTarget.append(angularCoefficient)
        self.__funcTarget.append(constan)

    def __createDataSet(self, size):
        x = []
        y = []
        for i in range(size):
            x0 = self.__generateValueBetween()
            x1 = self.__generateValueBetween()
            x.append([x0,x1])
            y.append(self.__getValueY(x0, x1))

        return x, y

    def __getValueY(self, x0, x1):
        value = self.__funcTarget[0]*x0+self.__funcTarget[1] - x1
        y = 1
        if value > 0:
            y = 0
        return y

    def __generateValueBetween(self, first= -1, second = 1):
        value = random.uniform(first, second)
        return round( value, 3)
    # Verifica se a distribuicao esta com valores diferentes e não tods iguais do mesmo lado. Tambem garante uma distruibuicao
    # mais homogenea onde garante que os valores serão ao menos 3 de um lado e 7 do outro

    def __checkDistribution(self, y):
        isDifferent = False
        diferrents  = 0
        for i in range(len(y)-1):
            if y[i] != y[len(y)-1]:
                diferrents += 1
        if diferrents > 2 and diferrents < 7:
            print("Aqui")
            print(diferrents)
            isDifferent = True

        return isDifferent

