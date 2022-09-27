class graph:
    pointNum = 0
    isDirectional = False
    typeNum = ()
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
            target = [t, v]
            self.map[pointA] = target
            self.edgeNum = self.edgeNum + 1
            if self.map.get(pointB) is not None:
                data = self.map.get(pointB)
                t = data[0]
                v = data[1]
                t.append(pointA)
                v.append(type)
                target = [t, v]
                self.map[pointB] = target
            else:
                t = [pointA]
                v = [type]
                target = [t, v]
                self.map[pointB] = target
                self.pointNum = self.pointNum + 1
        else:
            t = [pointB]
            v = [type]
            target = [t, v]
            self.map[pointA] = target
            self.pointNum = self.pointNum + 1
            self.edgeNum = self.edgeNum + 1
            if self.map.get(pointB) is not None:
                data = self.map.get(pointB)
                t = data[0]
                v = data[1]
                t.append(pointA)
                v.append(type)
                target = [t, v]
                self.map[pointB] = target
            else:
                t = [pointA]
                v = [type]
                target = [t, v]
                self.map[pointB] = target
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
        return int(self.edgeNum / (self.pointNum / 2))
