import numpy as np
import utils

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
def subkey_generation (K, mode):
    if(mode == "n"):
        K_0 = [K[0],K[1],K[2],K[3]]
        K_1 = [K[0],K[1],K[3],K[2]]
        K_2 = [K[1],K[2],K[3],K[0]]
        K_3 = [K[0],K[3],K[1],K[2]]
        K_4 = [K[2],K[3],K[0],K[1]]
        K_5 = [K[1],K[3],K[0],K[2]]
    else:
        K_0 = [K[0],K[2],K[4],K[6]]
        K_1 = [K[0],K[1],K[2],K[3]]
        K_2 = [K[0],K[3],K[4],K[7]]
        K_3 = [K[0],K[3],K[5],K[6]]
        K_4 = [K[0],K[2],K[5],K[7]]
        K_5 = [K[2],K[3],K[4],K[5]]
    return K_0,K_1,K_2,K_3,K_4,K_5


"""
subkey_sum()
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
def subkey_sum (sub_key, w, p):
    v = list((w + np.array(sub_key+sub_key))%p)
    return v

"""
subkey_sub()
@description: sub_key sub function
@params:'sub_key' previously computed subkey of the original key K
        @type list of integers
        @dimension (1x4)
        'v' output of the previous time stap
        @type list of integers
        @dimension (1x8)
        'p' prime number
        @type integer
        @dimension (1x1)
@output:'w' result of the difference modulo p
        @type list of integers
        @dimension (1x8)
"""
def subkey_sub (sub_key, v, p):
    w = list((v - np.array(sub_key+sub_key))%p)
    return w

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
    
def linear_inverse(w,p):
    #Organization of the elements of w in a matrix
    matrix_W= np.array([w[:4],w[4:] ] ) 
    #Matrix called 'A_inverse' that is the inverse of matrix A 
    matrix_A_inverse= np.array([[2,8],[6,10]])
    #matrix multiplication
    matrix_Z=np.dot(matrix_A_inverse,matrix_W)
    # Mod p 
    matrix_Z= matrix_Z%p
    #Reorganization in a list
    z=list(matrix_Z[0,:4] ) + list (matrix_Z[1,:4])
    return (z)

def linear_substitution(v, p):
    f = lambda x: (2 * x) % p
    y = []
    for v_i in v:
        y.append(f(v_i))
    return y

def linear_substitution_inverse(y, p):
    f = lambda x: (utils.modular_inverse(2,p) * x) % p
    v = []
    for y_i in y:
        v.append(f(y_i))
    return v

def nearlyLinear_substitution(v):
    f = [0,2,4,8,6,10,1,3,5,7,9]
    y = []
    for v_i in v:
        y.append(f[int(v_i)])
    return y

def nearlyLinear_substitution_inverse(y):
    f = [0,2,4,8,6,10,1,3,5,7,9]
    v = []
    for y_i in y:
        for i in range(len(f)):
            if(f[i]==y_i):
                v.append(i)
    return v

def nonLinear_substitution(v, p):
    f = lambda x: 2 * utils.modular_inverse(x, p)
    y = []
    for v_i in v:
        if(v_i!=0):
            y.append(f(v_i))
        else:
            y.append(0)
    return y

def nonLinear_substitution_inverse(y,p):
    f = lambda x: 2 * utils.modular_inverse(x, p)
    v = []
    for y_i in y:
        if(y_i == 0):
            v.append(0)
        else:
            v.append(f(y_i))
    return v

