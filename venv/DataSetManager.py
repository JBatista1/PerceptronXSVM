import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

# Converter y para array de array para trabalahr com matrizes numpy
class DataSetManager:

    def __init__(self, classClassify):

        self.classClassify = classClassify
        self.iris = self.__load_dataset()
        self.X, self.Y = self.__splitDataset()
        self.__add_in_X_x0_equals_one()
        self.X_train, self.X_test, self.Y_train, self.Y_test = self.__create_datas()



    def __create_datas(self):
        X_train, X_test, Y_train, Y_test = train_test_split(self.X, self.Y, test_size=0.2, random_state=42)
        return X_train,X_test,Y_train,Y_test

    def get_data_X_Y_for_train_and_test(self):

        return self.X_train,self.X_test,self.Y_train,self.Y_test

    def __convert_Y_to_matrix(self, Y):
        size = len(Y)
        array = []
        for i in range(size):
            array.append(Y[i])
        return np.array(array)
    def __add_in_X_x0_equals_one(self):
        size = len(self.X)
        x0 = np.ones([size,1])
        self.X = np.concatenate((x0,self.X), axis=1)

    def __load_dataset(self):
        dataset = datasets.load_iris()
        return dataset

    def __convert_to_binary_rating(self, y):
        binaryArray = np.where(y == self.classClassify, 0, 1)
        return binaryArray

    def __splitDataset(self):
        X = self.iris.data
        Y = self.iris.target
        Y  = self.__convert_to_binary_rating(Y)
        Y = Y.reshape(len(Y),1)
        return X, Y
