import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


class Matrix:
    matrix = []
    ppi = []
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
        print(self.m)  # 19
        print(self.n)  # 383

    def init_ppi(self, file_path):
        f = open(file_path)
        line = f.readline()
        cnt = 0
        while line:
            datalist = line.split()
            self.ppi.append(list(map(int, datalist)))
            cnt = cnt + 1
            line = f.readline()

    def classify(self):
        for i in range(self.m):
            self.group.append([])
        for i in range(self.n):
            for j in range(self.m):
                if self.matrix[i][j] == 1:
                    self.group[j].append(i)

    def calculate(self):
        # print(self.group)
        # 先对矩阵进行降维
        global dis_e_group, dis_c_group
        pca = PCA(n_components='mle')
        ppi_ = pca.fit_transform(self.ppi)
        print(len(ppi_[0]))
        intra_dis_eucl = []
        intra_dis_cos = []
        inter_dis_eucl = []
        inter_dis_cos = []
        np.seterr(divide='ignore', invalid='ignore')
        for i in range(self.m):
            dis_e = 0
            dis_c = 0
            for j in range(len(self.group[i])):
                a = np.array(ppi_[self.group[i][j]])
                for k in range(len(self.group[i])):
                    if j == k:
                        continue
                    b = np.array(ppi_[self.group[i][k]])
                    dis_e += np.linalg.norm(a - b)
                    dis_c += 1 - (np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

            num = (len(self.group[i]) * len(self.group[i]))-len(self.group[i])
            if len(self.group[i]) == 1:
                num = num+1
            intra_dis_eucl.append(format(dis_e / num, '.3f'))
            intra_dis_cos.append(format(dis_c / num, '.3f'))

        for i in range(self.m):
            dis_e_group = 0
            dis_c_group = 0
            for ii in range(self.m):
                dis_e = 0
                dis_c = 0
                for j in range(len(self.group[i])):
                    a = np.array(ppi_[self.group[i][j]])
                    for jj in range(len(self.group[ii])):
                        b = np.array(ppi_[self.group[ii][jj]])
                        if i == ii:
                            dis_e += 0
                            dis_c += 0
                            break
                        else:
                            dis_e += np.linalg.norm(a - b)
                            dis_c += 1 - (np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

                dis_e_group += (dis_e / (len(self.group[i]) * len(self.group[ii])))
                dis_c_group += (dis_c / (len(self.group[i]) * len(self.group[ii])))

            inter_dis_eucl.append(format(dis_e_group / (self.m - 1), '.3f'))
            inter_dis_cos.append(format(dis_c_group / (self.m - 1), '.3f'))

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
