import numpy as np

def modular_inverse(a,m):
    for x in range(1,m):
        if((a%m)*(x%m) % m==1):
            return x
    raise Exception('The modular inverse does not exist.')

def matrix_inverse(A,p):
    A_inv = np.linalg.inv(A)
    det_a = round((np.linalg.det(A)))
    det_a_inv = modular_inverse(det_a,p)
    return (det_a * A_inv * det_a_inv)%p


def read_file(path):
    file = open(path, "r")
    u = []
    x = []
    for line in file:
        tmp = line.split("]")
        u_i = tmp[0].split("[")
        u_i = np.array(u_i[1].split(",")).astype(int)
        x_i = tmp[1].split("[")
        x_i = np.array(x_i[1].split(",")).astype(int)
        u.append(u_i)
        x.append(x_i)
    return u,x