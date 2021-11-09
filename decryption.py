import cipher
import encryption as e

#   Decryption mode:
#   -l linear
#   -nl nearly linear
#   -n non linear

def decryption(x, K, mode):
    v=[]
    y=[]
    z=[]
    p = 11
    k_i = cipher.subkey_generation(K, mode)
    n = 5
    v = x
    
    z = cipher.subkey_sub(k_i[n],v,p)
    for i in range(n-1,-1,-1):
        if(i<n-1):
            z = cipher.linear_inverse(w,p)
        y = cipher.transposition(z)
        if(mode == "l"):
            v = cipher.linear_substitution_inverse(y,p)
        elif(mode == "nl"):
            v = cipher.nearlyLinear_substitution_inverse(y)
        elif(mode == "n"):
            v = cipher.nonLinear_substitution_inverse(y,p)
        w = cipher.subkey_sub(k_i[i],v,p)
    u = w

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

    K = [1,0,0,0,0,0,0,0] #key space
    x =  e.encryption([1,2,3,4,5,6,7,8],K,"nl") #plain text

    print()
    print("[*] Nearly linear decryption")
    print(" x:", x)
    print(" K:", K)
    print(" u:", decryption(x, K, "nl"))
    print()

    K = [1,0,0,0] #key space
    x =  e.encryption([1,2,3,4,5,6,7,8],K,"n") #plain text

    print()
    print("[*] Non linear decryption")
    print(" x:", x)
    print(" K:", K)
    print(" u:", decryption(x, K, "n"))
    print()
