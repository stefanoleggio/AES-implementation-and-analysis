def encryption():
    #variables
    K = [1,0,0,0,0,0,0,0] #key space
    u = [1,0,0,0,0,0,0,0] #plain text
    x = [] #cipher text
    v=[] #output of k_i+u additon
    y=[] #output of substitution
    z=[] #output of transposition
    w=[] #output of linear

    '''
        1) generate subkeys
        2) 5 rounds k_i+u, S, T, L
        3) last round different: just S T and k_i+u
        4) get x
    '''


if __name__ == "__main__":
    encryption()