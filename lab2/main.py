import adjMatrix
import  interactionMatrix
if __name__ == '__main__':
    handle = adjMatrix.Matrix()
    handle.__int__(383)
    file_path = "../file/pdi.txt"
    handle.init_pdi(file_path)
    file_path = "../file/ppi.txt"
    handle.init_matrix(file_path)
    handle.embedding()

    handle_ = interactionMatrix.Matrix()
    handle_.__int__()
    file_path = "../file/pdi.txt"
    handle_.init_matrix(file_path)
    file_path = "../file/ppi.txt"
    handle_.init_ppi(file_path)
    handle_.classify()
    handle_.calculate()