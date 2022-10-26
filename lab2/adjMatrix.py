# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class Matrix:
    m = []
    n = 0
    pdi = []
    group = []
    def __int__(self, size):
        self.n = size
        self.m = [[0] * size] * size

    def init_matrix(self, file_path):
        f = open(file_path)
        line = f.readline()
        cnt = 0
        while line:
            datalist = line.split()
            self.m[cnt] = list(map(int, datalist))
            cnt = cnt + 1
            line = f.readline()
    def init_pdi(self, file_path):
        f = open(file_path)
        line = f.readline()
        cnt = 0
        while line:
            datalist = line.split()
            self.pdi.append(list(map(int, datalist)))
            cnt = cnt + 1
            line = f.readline()


    def classify(self):
        for i in range(19):
            self.group.append([])
        for i in range(383):
            for j in range(19):
                if self.m[i][j] == 1:
                    self.group[j].append(i)
    def embedding(self):
        self.classify()  # 分类

        src = np.array(self.m)
        feature = np.linalg.eig(np.cov(src.T))
        feature_pairs = [((np.abs(feature[0][i])), feature[1][:, i]) for i in range(len(feature[0]))]
        feature_pairs.sort(reverse=True)
        best_feature = feature_pairs[0][1]

        src = src - src.mean(axis=0)
        dst = np.transpose(np.dot(best_feature, np.transpose(src)))
        # dst = src.dot(best_feature)

        hot_matrix = [[0] * self.n] * self.n
        hot_matrix_ = [[0] * self.n] * self.n
        _hot_matrix = []
        map = []
        index = {}
        for i in range(self.n):
            hot_matrix[i] = np.abs(dst - dst[i])
            map.append(0)

        for i in range(self.n):
            index.update({abs(dst[i]): i})

        index = sorted(index.items(), reverse=True)
        index = list(index)
        print(index)
        for i in range(self.n):
            hot_matrix_[i] = hot_matrix[index[i][1]]

        for i in range(len(self.group)):
            for j in range(len(self.group[i])):
                if(map[self.group[i][j]] == 0):
                    _hot_matrix.append(hot_matrix[self.group[i][j]])
                    map[self.group[i][j]] = 1

        hot_matrix = np.array(hot_matrix)
        #hot_matrix = hot_matrix[0:60,0:60]
        hot_matrix_ = np.array(hot_matrix_)
        #hot_matrix_ = hot_matrix_[0:60,0:60]
        _hot_matrix = np.array(_hot_matrix)


        f, (ax1, ax2, ax3) = plt.subplots(figsize=(10, 10), nrows=3)
        sns.heatmap(hot_matrix, ax=ax1, cmap='RdBu_r', center=0, square=True)
        #sns.heatmap(hot_matrix, ax=ax1 ,square=True)
        sns.heatmap(hot_matrix_, ax=ax2, cmap='RdBu_r', center=0, square=True)
        sns.heatmap(_hot_matrix, ax=ax3, cmap='RdBu_r', center=0, square=True)
        plt.title("heatmap")
        plt.savefig('../output/hotmap.png')
        plt.show()
