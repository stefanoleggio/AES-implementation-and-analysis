import cipher

#   Encryption mode:
#   -l linear
#   -nl nearly linear
#   -n non linear

def encryption(u, K, mode):
    x = [] #cipher text
    v=[] #output of k_i+u additon
    y=[] #output of substitution
    z=[] #output of transposition
    p = 11

    k_i = cipher.subkey_generation(K)

    w = u
    n = 5 #number of round

    for i in range(0,n):
        v = cipher.subkey_sum(k_i[i],w,p)
        if(mode == "l"):
            y = cipher.linear_substitution(v, p)
        elif(mode == "nl"):
            y = cipher.nearlyLinear_substitution(v)
        elif(mode == "n"):
            y = cipher.nonLinear_subsitution(v, p)
        else:
            print("Invalid mode")
            return -1
        z = cipher.transposition(y)
        if(i<n-1): w = cipher.linear(z, p)
    x = cipher.subkey_sum(k_i[n],z,p)

    return x

if __name__ == "__main__":

    K = [1,0,0,0,0,0,0,0] #key space
    u = [1,0,0,0,0,0,0,0] #plain text

    print()
    print("[*] Linear encryption")
    print(" u:", u)
    print(" K:", K)
    print(" x:", encryption(u, K, "l"))
    print()
    print("[*] Nearly linear encryption")
    print(" u:", u)
    print(" K:", K)
    print(" x:", encryption(u, K, "nl"))
    print()
    print("[*] Non linear encryption")
    print(" u:", u)
    print(" K:", K)
    print(" x:", encryption(u, K, "n"))
    print()