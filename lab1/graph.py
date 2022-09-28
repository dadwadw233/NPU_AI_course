import matplotlib.pyplot as plt
import numpy as np
import matplotlib

import sys
sys.setrecursionlimit(100000)

matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号


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
    def add_point(self,point):
        self.map[point] = [[],[]]
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
        x = []
        y = []
        cnt = 0
        for i in data:
            x.append(i[0])
            y.append(i[1] / self.pointNum)

        x = np.array(x)
        y = np.array(y)
        # plt.hist(data_, density=True, bins=len(data_), facecolor="blue", edgecolor="blue")
        plt.bar(x, y)
        plt.xlabel("k")
        plt.ylabel("P(k)")
        plt.title("Degree Distribution")
        plt.show()

    def cal_min_value_path(self, start, end):
        # 初始化集合s
        s = {start: [[[start]], 0]}
        u = {}
        # 初始化集合u中与start直接连通的节点
        for i in range(len(self.map[start][0])):
            temp = [[[start, self.map[start][0][i]]], 1]
            u[self.map[start][0][i]] = list.copy(temp)
        # 初始化u中其他不直接与起点连通的节点
        for i in self.map:
            if i == start:
                continue
            elif u.get(i) is None:
                noData = [[[]], 114514]
                u[i] = noData
            else:
                continue

        while len(u) != 0:
            u_ = sorted(u.items(), key=lambda kv: kv[1][1])  # 对字典U按照value进行排序
            target = u_[0][0]
            pathList = u_[0][1][0]
            tempValue = u_[0][1][1]
            # 更新s
            s[target] = list.copy([pathList, tempValue])
            # 更新u
            u.pop(target)
            if self.map.get(target) is None:
                continue

            else:
                pointList = self.map.get(target)[0]
                valueList = self.map.get(target)[1]

            for i in range(len(pointList)):
                point = pointList[i]
                target2pointValue = valueList[i]
                start2targetPath = s[target][0]
                start2targetValue = s[target][1]
                if point == start:
                    continue
                if(u.get(point) is None):
                    continue
                start2pointValue = u[point][1]



                if start2targetValue + 1 < start2pointValue:
                    u[point][0].clear()
                    for j in range(len(start2targetPath)):
                        newPath = list.copy(start2targetPath[j])
                        newPath.append(point)
                        u[point][0].append(newPath)
                    u[point][1] = start2targetValue + 1

                elif start2targetValue + 1 == start2pointValue:
                        for j in range(len(start2targetPath)):
                            newPath = list.copy(start2targetPath[j])
                            newPath.append(point)
                            u[point][0].append(newPath)
                else:
                    continue

        return s[end]

    def get_clustering_coefficient(self):
        dist = {}
        sum = 0
        pointList = sorted(self.map)
        for i in pointList:
            e = 0
            neighbors = list.copy(self.map[i][0])
            k = len(neighbors)

            for j in neighbors:
                for h in neighbors:
                    if i == j:
                        continue
                    else:
                        temp = list.copy(self.map[j][0])
                        if temp.count(h) == 1:
                            e = e+1
                        else:
                            continue
            if k == 1:
                c = 0
            else:
                c = e / (k * (k - 1))

            sum = sum + c
            dist[i] = format(c,'.3f')

        print("每个点的聚集系数：")
        print(dist)
        print("平均聚集系数")
        print('%.3f' %(sum/len(pointList)))

    def get_connected_component_num(self):
        sum = 0;
        check = {}
        pointList = sorted(self.map)
        start = pointList[0]
        while len(pointList) != 0:
            start = pointList[0]
            self.dfs_loop(start, pointList)
            sum = sum+1

        print(sum)
    def dfs_loop(self,n,pointList):
        if len(self.map[n][0]) == 0:
            pointList.remove(n)
            return
        for i in self.map[n][0]:
            if pointList.count(i) == 1:
                pointList.remove(i)
                self.dfs_loop(i, pointList)
            else:
                continue

    def get_Q8_result(self):
        pointList = sorted(self.map)
        sum = 0
        for i in pointList:
            value = list.copy(self.map[i][1])
            if value.count(47) < 2:
                continue
            else:
                indexList = []
                for j in range(len(value)):
                    if value[j] == 47:
                        indexList.append(j)
                    else:
                        continue
            for m in indexList:
                for n in indexList:
                    pointA = self.map[i][0][m]
                    pointB = self.map[i][0][n]
                    if m == n :
                        continue
                    else:
                        if (self.map[pointA][0]).count(pointB) == 0:
                            continue
                        else:
                            temp = (self.map[pointA][0]).index(pointB)
                            if(self.map[pointA][1][temp] == 73):
                                sum = sum+1
                            else:
                                continue
        return int(sum/2)






