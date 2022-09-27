class graph:
    point = 0
    isDirectional = False
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
        else:
            source = pointA
            t = [pointB]
            v = [type]
            target = [t, v]
            self.map[pointA] = target

    def print_(self):
        data = self.map.get(0)
        print(data)
