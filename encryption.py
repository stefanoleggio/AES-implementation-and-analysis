import cipher

def encryption():
    #variables
    K = [1,0,0,0,0,0,0,0] #key space
    u = [1,0,0,0,0,0,0,0] #plain text
    x = [] #cipher text
    v=[] #output of k_i+u additon
    y=[] #output of substitution
    z=[] #output of transposition
    p = 11

    k_i = cipher.subkey_generation(K)

    w = u
    n = 5 #number of round

    for i in range(0,n):
        v = cipher.addition(k_i[i],w,p)
        y = cipher.linear_substitution(v, p)
        z = cipher.transposition(y)
        if(i<n-1): w = cipher.linear(z, p)
    x = cipher.addition(k_i[n],z,p)

    print("x: ", x)


if __name__ == "__main__":
    encryption()
