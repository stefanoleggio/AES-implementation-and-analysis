import encryption as e
import decryption as d
import utils
import numpy as np
import time
import itertools

if __name__ == "__main__":

    K = [] # List for all possible keyset
    kx_pairs = [] # List for key and cipher text
    ku_pairs = [] # List for key and plain text

    U, X = utils.read_file("KPAdataAerosmith/KPApairsAerosmith_non_linear.txt")

    print("[*] Creating K set")

    start_time = time.time()

    # Creates all the possible combinatios of a four element list with values 0-10
    K = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9,10], 4))

    print(" Total keys: ", len(K))


    iterations=0
    total_iterations = 0
    print("[*] Generating all possible u and x")
    for k in K:
        for u,x in zip(U,X):
            iterations+=1

            if(iterations > 10000): # Print a message each 1000 iterations
                total_iterations += iterations
                iterations = 0
                print(" Total pairs created:", total_iterations*2)
            
            # Encrypt message u with key k
            x_i = e.encryption(u,k,"n")

            # Decrypt message x with key k
            u_i = d.decryption(x,k,"n")

            # Converting the list [a,b,c...] in a number abc... in order to be able to sorting the list

            s_x = ""
            for j in x_i:
                s_x = s_x + str(j)

            s_u = ""
            for j in u_i:
                s_u = s_u + str(j)

            # Inserting the pairs in the list

            kx_pairs.append([int(s_x),k])
            ku_pairs.append([int(s_u),k])
    
    print(" Total cipher texts generated: ", len(kx_pairs))
    print(" Total plain texts generated: ", len(ku_pairs))

    print("[*] Sorting pairs lists")

    # Sorting lists by the message (ciphertext or plaintext)

    kx_pairs.sort()
    ku_pairs.sort()

    # Copy all the messages values in a separate list in order to make the search easy

    x_values = []
    u_values = []
    for kx in kx_pairs:
        x_values.append(kx[0])
    for ku in ku_pairs:
        u_values.append(ku[0])

    print("[*] Searching matchings")

    k1 = []
    k2 = []
    k_counter = 0

    # Find all possible matching where the plain text is equal to the cipher text

    for i in range(len(x_values)):
        index = np.searchsorted(u_values, x_values[i])
        if(x_values[i]==u_values[index]):
            print("[*] Match founded!")
            tmp_k1 = kx_pairs[i][1]
            tmp_k2 = ku_pairs[index][1]
            print(" k1 =", tmp_k1)
            print(" k2 =", tmp_k2)
            print("[*] Check if the keys are valid")

            # Since all the ciphertext in the file are encrypted with the same key I try to encrypt the first value
            
            x_1 = e.encryption(e.encryption(U[0],tmp_k1,"n"),tmp_k2,"n")
            if((x_1 == X[0]).all()):
                print(" The keys are valid!")
                break
            else:
                print(" The keys are not valid")
            k1.append(tmp_k1)
            k2.append(tmp_k2)
    print("----- Total execution time:", (time.time() - start_time), "seconds -----")