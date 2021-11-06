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
