"""
subkey_generation()
@description: sub_key generating function
@params:'K' the original key
        @type array of integers
        @dimension (1x8)
@output:'K_0','K_1','K_2','K_3','K_4','K_5' generated subkeys
        @type array of integers
        @dimension (1x4)
"""
def subkey_generation (K):
    K_0 = np.array([K[0],K[2],K[4],K[6]])
    K_1 = np.array([K[0],K[1],K[2],K[3]])
    K_2 = np.array([K[0],K[3],K[4],K[7]])
    K_3 = np.array([K[0],K[3],K[5],K[6]])
    K_4 = np.array([K[0],K[2],K[5],K[7]])
    K_5 = np.array([K[2],K[3],K[4],K[5]])
    return K_0,K_1,K_2,K_3,K_4,K_5

