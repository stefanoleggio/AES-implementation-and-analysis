def linear(z,p):
    #Organization of the elements of z in a matrix
    matrix_Z= np.array([z[:4],z[4:] ] ) 
    print (matrix_Z)
    #Matrix called 'A' that is fixed in this function
    matrix_A= np.array([[2,5],[1,7]])
    print(matrix_A)
    #matrix multiplication
    matrix_W=np.dot(matrix_A,matrix_Z)
    print(matrix_W)
    # Mod p 
    matrix_W= matrix_W%p
    print(matrix_W)
    #Reorganization in a list
    w=list(matrix_W[0,:4] ) + list (matrix_W[1,:4])
    print (w)
    return (w)
