import cipher

#   Decryption mode:
#   -l linear
#   -nl nearly linear
#   -n non linear

def decryption(x, K, mode):
    v=[]
    y=[]
    z=[]
    p = 11
    k_i = cipher.subkey_generation(K)
    n = 5
    v = x
    
    for i in range(n,0,-1):
        if(i<n):
            v = cipher.linear_inverse(z,p)
        z = cipher.subkey_sub(k_i[i],v,p)
        y = cipher.transposition(z)
        v = cipher.linear_substitution_inverse(y,p)

    u = cipher.subkey_sub(k_i[0],v,p)

    return u


if __name__ == "__main__":

    K = [1,0,0,0,0,0,0,0] #key space
    x = [4,0,0,9,7,0,0,3] #plain text

    print()
    print("[*] Linear decryption")
    print(" x:", x)
    print(" K:", K)
    print(" u:", decryption(x, K, "l"))
    print()