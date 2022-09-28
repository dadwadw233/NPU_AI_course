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


    print("**********************************************************************")
    print("Q5")
    #handle.clean()

    #handle.add(0,1,5)
    #handle.add(0,2,2)
    #handle.add(0,4,3)
    #handle.add(0,3,2)
    #handle.add(3,4,1)
    #handle.add(1,2,1)
    print("8到309的所有最短路：")
    print(handle.cal_min_value_path(8, 309)[0])
    print("67到850的所有最短路：")
    print(handle.cal_min_value_path(67, 850)[0])
    print("990到1256的所有最短路：")
    print(handle.cal_min_value_path(990, 1256)[0])

    print("**********************************************************************")
    print("Q6")
    handle.get_clustering_coefficient()

    print("**********************************************************************")
    print("Q7")
    handle.clean()

    handle.add(0,1,1)
    handle.add(1,2,1)
    handle.add(1,3,1)
    handle.add(2,3,1)

    handle.add_point(4)
    handle.add(4,5,1)
    handle.add_point(6)
    handle.get_connected_component_num()

    print("**********************************************************************")
    print("Q8")
    handle.clean()
    f = open("../file/ddi_with_type_latest.txt")
    line = f.readline()
    cnt = 0
    while line:
        datalist = line.split()
        handle.add(int(datalist[0]), int(datalist[1]), int(datalist[2]))
        line = f.readline()
        cnt = cnt + 1

    print(handle.get_Q8_result())