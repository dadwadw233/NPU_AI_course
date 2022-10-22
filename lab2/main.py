import adjMatrix

if __name__ == '__main__':
    handle = adjMatrix.Matrix()
    handle.__int__(383)
    file_path = "../file/ppi.txt"
    handle.init_matrix(file_path)
    handle.embedding()