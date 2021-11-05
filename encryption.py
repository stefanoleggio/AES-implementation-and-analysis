import addition
import subkey_generation
import substitution
import transposition
import linear

def encryption():
    #variables
    K = [1,0,0,0,0,0,0,0] #key space
    u = [1,0,0,0,0,0,0,0] #plain text
    x = [] #cipher text
    v=[] #output of k_i+u additon
    y=[] #output of substitution
    z=[] #output of transposition
    p = 11

    k_i = subkey_generation.subkey_generation(K)

    w = u
    n = 5 #number of round

    for i in range(0,n-2):
        v = addition.addition(k_i[i],w,p)
        y = substitution.linear_substitution(v, p)
        z = transposition.transposition(y)
        w = linear.linear(z, p)

    v = addition.addition(k_i[n-1],w,p)
    y = substitution.linear_substitution(v, p)
    z = transposition.transposition(y)
    x = addition.addition(k_i[n],w,p)

    print()
    print("x: ", x)


if __name__ == "__main__":
    encryption()