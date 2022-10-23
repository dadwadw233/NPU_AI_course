import numpy
import numpy as np
import matplotlib.pyplot as plt
import pandas
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
        # print(self.m)

    def classify(self):
        for i in range(self.m):
            self.group.append([])
        for i in range(self.n):
            for j in range(self.m):
                if self.matrix[i][j] == 1:
                    self.group[j].append(i)

    def calculate(self):
        # print(self.group)
        intra_dis_eucl = []
        intra_dis_cos = []
        inter_dis_eucl = []
        inter_dis_cos = []
        np.seterr(divide='ignore', invalid='ignore')
        for i in range(self.m):
            dis_e = 0
            dis_c = 0
            for j in range(len(self.group[i])):
                a = np.array(self.matrix[self.group[i][j]])
                for k in range(len(self.group[i])):
                    b = np.array(self.matrix[self.group[i][k]])
                    dis_e += np.linalg.norm(a - b)
                    dis_c += 1 - (np.dot(a, b) / (np.sqrt(np.sum(np.square(a))) * np.sqrt(np.sum(np.square(b)))))

            intra_dis_eucl.append(dis_e / (len(self.group[i]) * len(self.group[i])))
            intra_dis_cos.append(dis_c / (len(self.group[i]) * len(self.group[i])))

        dis_e = 0
        dis_c = 0
        dis_e_group = 0
        dis_c_group = 0
        for i in range(self.m):
            for ii in range(self.m):
                for j in range(len(self.group[i])):
                    a = np.array(self.matrix[self.group[i][j]])
                    for jj in range(len(self.group[ii])):
                        b = np.array(self.matrix[self.group[ii][jj]])
                        if i == ii:
                            dis_e += 0
                            dis_c += 0
                        else:
                            dis_e += np.linalg.norm(a - b)
                            dis_c += 1 - (np.dot(a, b) / (np.sqrt(np.sum(np.square(a))) * np.sqrt(np.sum(np.square(b)))))
                dis_e_group += (dis_e / (len(self.group[i]) * len(self.group[ii])))
                dis_c_group += (dis_c / (len(self.group[i]) * len(self.group[ii])))

            inter_dis_eucl.append(dis_e_group / (self.m * self.m))
            inter_dis_cos.append(dis_c_group / (self.m * self.m))
            dis_c_group = 0
            dis_e_group = 0


        maxlen = 0
        for i in range(self.m):
            if len(self.group[i]) > maxlen:
                maxlen = len(self.group[i])
        print(maxlen)
        col = []
        for i in range(maxlen):
            col.append("protein" + str(i + 1))
        row = []
        for i in range(self.m):
            row.append("disease" + str(i + 1))

        data = self.group.copy()
        for i in range(self.m):
            for j in range(len(data[i])):
                data[i][j] = 'P' + str(data[i][j] + 1)
            for j in range(maxlen - len(data[i])):
                data[i].append("none")

        data = np.array(data)

        plt.figure(figsize=(150, 4), dpi=100)
        tab = plt.table(cellText=data, colLabels=col, rowLabels=row, cellLoc="center", loc='center')

        plt.axis('off')
        # plt.savefig('../output/di.png')
        plt.show()

        col = []
        col.append("Intra-class(Euclidean)")
        col.append("Intra-class(cosine)")
        col.append("Inter-class(Euclidean)")
        col.append("Inter-class(cosine)")
        data = []
        for i in range(self.m):
            data.append([])
            data[i].append(intra_dis_eucl[i])
            data[i].append(intra_dis_cos[i])
            data[i].append(inter_dis_eucl[i])
            data[i].append(inter_dis_cos[i])

        data = np.array(data)

        plt.figure(figsize=(10, 10), dpi=100)
        tab_ = plt.table(cellText=data, colLabels=col, rowLabels=row, cellLoc="center", loc='center')

        plt.axis('off')
        plt.savefig('../output/ans.png')
        plt.show()
