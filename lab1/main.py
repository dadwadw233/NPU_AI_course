#-*- coding: UTF-8 -*-
import graph

if __name__ == '__main__':
    handle = graph.graph()
    handle.add(1, 2, 1)
    handle.add(1, 4, 3)
    handle.add(2, 4, 1)
    handle.add(4, 3, 2)
    test = handle.get_point_num()

    print("Q1")
    print("网络中节点的数量为:")
    print(test)
    test = handle.get_edge_num()
    handle.draw_normalized_histogram()
    print("网络中边的数量为:")
    print(test)
    print("**********************************************************************")
    print("Q2")
    print("度最大的前三个节点依次是：")
    print(handle.get_top_n_point(3))
    print("节点的平均度:")
    print(handle.get_average_degree())
    print("**********************************************************************")
    print("Q3")
    handle.clean()
    f = open("../file/ddi_with_type_latest.txt")
    line = f.readline()
    cnt = 0
    while line:
        datalist = line.split()
        handle.add(int(datalist[0]), int(datalist[1]), int(datalist[2]))
        line = f.readline()
        cnt = cnt+1
    print("边的类型数：")
    print(handle.get_type_num())
    print("类型为47的边的条数:")
    print(handle.count_type(47))

    print("**********************************************************************")
    print("Q4")
    handle.draw_normalized_histogram()