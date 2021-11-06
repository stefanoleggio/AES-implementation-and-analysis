import numpy as np

"""
subkey_generation()
@description: sub_key generating function
@params:'K' the original key
        @type list of integers
        @dimension (1x8)
@output:'K_0','K_1','K_2','K_3','K_4','K_5' generated subkeys
        @type list of integers
        @dimension (1x4)
"""
def subkey_generation (K):
    K_0 = [K[0],K[2],K[4],K[6]]
    K_1 = [K[0],K[1],K[2],K[3]]
    K_2 = [K[0],K[3],K[4],K[7]]
    K_3 = [K[0],K[3],K[5],K[6]]
    K_4 = [K[0],K[2],K[5],K[7]]
    K_5 = [K[2],K[3],K[4],K[5]]
    return K_0,K_1,K_2,K_3,K_4,K_5


"""
addition()
@description: sub_key sum function
@params:'sub_key' previously computed subkey of the original key K
        @type list of integers
        @dimension (1x4)
        'w' output of the previous time stap
        @type list of integers
        @dimension (1x8)
        'p' prime number
        @type integer
        @dimension (1x1)
@output:'v' result of the summations modulo p
        @type list of integers
        @dimension (1x8)
"""
def addition (sub_key, w, p):
    v = list((w + np.array(sub_key+sub_key))%p)
    return v

def transposition(y):
    #transposition of the second half 
    y[4], y[5], y[6], y[7]= y[7], y[6], y[5], y[4]
    z=y
    return z

def linear(z,p):
    #Organization of the elements of z in a matrix
    matrix_Z= np.array([z[:4],z[4:] ] ) 
    #Matrix called 'A' that is fixed in this function
    matrix_A= np.array([[2,5],[1,7]])
    #matrix multiplication
    matrix_W=np.dot(matrix_A,matrix_Z)
    # Mod p 
    matrix_W= matrix_W%p
    #Reorganization in a list
    w=list(matrix_W[0,:4] ) + list (matrix_W[1,:4])
    return (w)

def linear_substitution(v, p):
    f = lambda x: (2 * x) % p
    y = []
    for v_i in v:
        y.append(f(v_i))
    return y

def nearlylinear_substitution(v, p):
    f = [0,2,4,8,6,10,1,3,5,7,9]
    y = []
    for v_i in v:
        y.append(f[v_i])
    return y

