#-*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Matrix:
    m = []
    n = 0

    def __int__(self, size):
        self.n = size
        self.m = [[0] * size] * size

    def init_matrix(self,file_path):
        f = open(file_path)
        line = f.readline()
        cnt = 0
        while line:
            datalist = line.split()
            self.m[cnt] = list(map(int,datalist))
            cnt = cnt+1
            line = f.readline()

    def embedding(self):
        src = np.array(self.m)
        feature = np.linalg.eig(np.cov(src.T))
        feature_pairs = [((np.abs(feature[0][i])), feature[1][:,i])for i in range(len(feature[0]))]
        feature_pairs.sort(reverse=True)
        best_feature = feature_pairs[0][1]

        src = src-src.mean(axis=0)
        dst = np.transpose(np.dot(best_feature,np.transpose(src)))
        #dst = src.dot(best_feature)

        hot_matrix = [[0] * self.n] * self.n

        for i in range(self.n):
            hot_matrix[i] = np.abs(dst-dst[i])

        hot_matrix = np.array(hot_matrix)
        hot_matrix = hot_matrix[0:20,0:20]
        f,(ax1,ax2) = plt.subplots(figsize=(20,20),nrows=2)
        sns.heatmap(hot_matrix,ax=ax1)
        plt.show()


