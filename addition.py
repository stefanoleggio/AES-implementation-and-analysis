"""
addition()
@description: sub_key sum function
@params:'sub_key' previously computed subkey of the original key K
        @type array of integers
        @dimension (1x4)
        'w' output of the previous time stap
        @type array of integers
        @dimension (1x8)
        'p' prime number
        @type integer
        @dimension (1x1)
@output:'v' result of the summations modulo p
        @type array of integers
        @dimension (1x8)
"""

def addition (sub_key, w, p):
    v = (w + np.concatenate((sub_key,sub_key),axis=None))%p
    return v