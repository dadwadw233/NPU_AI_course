import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rcParams['axes.unicode_minus']=False     # 正常显示负号
class graph:
    pointNum = 0
    isDirectional = False
    typeNum = []
    edgeNum = 0
    map = {}

    def __int__(self, isDirectional_):
        self.isDirectional = isDirectional_

    def add(self, pointA, pointB, type):
        if self.map.get(pointA) is not None:
            data = self.map.get(pointA)
            t = data[0]
            v = data[1]
            t.append(pointB)
            v.append(type)
            self.typeNum.append(type)
            target = [t, v]
            self.map[pointA] = target
            self.edgeNum = self.edgeNum + 1
            if self.map.get(pointB) is not None and self.isDirectional is False:
                data = self.map.get(pointB)
                t = data[0]
                v = data[1]
                t.append(pointA)
                v.append(type)
                target = [t, v]
                self.map[pointB] = target
            elif self.isDirectional is False:
                t = [pointA]
                v = [type]
                target = [t, v]
                self.map[pointB] = target
                self.pointNum = self.pointNum + 1
            else:
                self.pointNum = self.pointNum + 1
        else:
            t = [pointB]
            v = [type]
            self.typeNum.append(type)
            target = [t, v]
            self.map[pointA] = target
            self.pointNum = self.pointNum + 1
            self.edgeNum = self.edgeNum + 1
            if self.map.get(pointB) is not None and self.isDirectional is False:
                data = self.map.get(pointB)
                t = data[0]
                v = data[1]
                t.append(pointA)
                v.append(type)
                target = [t, v]
                self.map[pointB] = target
            elif self.isDirectional is False:
                t = [pointA]
                v = [type]
                target = [t, v]
                self.map[pointB] = target
                self.pointNum = self.pointNum + 1
            else:
                self.pointNum = self.pointNum + 1

    def print_(self):
        for i in self.map:
            print(i)
            print(self.map[i])

    def get_point_num(self):
        return self.pointNum

    def get_edge_num(self):
        return self.edgeNum

    def get_top_n_point(self, n):
        ans = []
        temp = sorted(self.map.items(), key=lambda kv: len(kv[1][0]), reverse=True)
        temp = list(temp)
        for i in range(n):
            ans.append(temp[i][0])
        return ans

    def get_map(self):
        print(self.map)

    def get_average_degree(self):
        return self.edgeNum * 2 / self.pointNum

    def clean(self):
        self.map.clear()
        self.typeNum.clear()
        self.edgeNum = 0
        self.pointNum = 0

    def get_type_num(self):
        return len(set(self.typeNum))

    def count_type(self, key):
        return self.typeNum.count(key)

    def test(self):
        return len(self.map[1][0])

    def draw_normalized_histogram(self):
        maxnum = 0;
        sum = self.pointNum
        data = {}
        for i in self.map:
            cnt = len(self.map[i][0])
            if data.get(cnt) is None:
                data[cnt] = 1
            else:
                data[cnt] = data[cnt] + 1
        data = sorted(data.items(), key=lambda kv: kv[0])
        data_ = []
        for i in data:
            data_.append(i[1])

        data_ = np.array(data_)
        print(data_)
        plt.hist(data_, density=True, bins=len(data_), facecolor="blue", edgecolor="blue")

        plt.xlabel("k")
        plt.ylabel("P(k)")
        plt.title("Degree Distribution")
        plt.show()
