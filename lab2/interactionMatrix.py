import numpy
import numpy as np


class Matrix:
    matrix = []
    n = 0
    m = 0
    group = []

    def __int__(self):
        self.n = 0
        self.m = 0

    def init_matrix(self, file_path):
        f = open(file_path)
        line = f.readline()
        cnt = 0
        while line:
            datalist = line.split()
            self.matrix.append(list(map(int, datalist)))
            cnt = cnt + 1
            line = f.readline()

        self.n = len(self.matrix)
        self.m = len(self.matrix[0])
        print(self.m)

    def classify(self):

        for i in range(self.n):
            for j in range(self.m):
                self.group.append([])
                if self.matrix[i][j] == 1:
                    self.group[j].append(i)

    def calculate(self):
        print(self.group)
        intra_dis_eucl = []
        intra_dis_cos = []
        inter_dis_eucl = []
        inter_dis_cos = []
        np.seterr(divide='ignore', invalid='ignore')
        for i in range(self.m):
            dis_e = 0
            dis_c = 0
            for j in range(len(self.group[i])):
                a = np.array(self.group[i][j])
                for k in range(len(self.group[i])):
                    b = np.array(self.group[i][k])
                    dis_e += np.linalg.norm(a-b)
                    dis_c += 1 - np.dot(a, b) / (np.sqrt(np.sum(np.square(a))) * np.sqrt(np.sum(np.square(b))))
            intra_dis_eucl.append(dis_e / (len(self.group[i]) * len(self.group[i])))
            intra_dis_cos.append(dis_c / (len(self.group[i]) * len(self.group[i])))

        print(intra_dis_eucl)
        print(intra_dis_cos)
