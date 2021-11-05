def linear_substitution(v, p):
    f = lambda x: 2 * x % p
    y = []
    for v_i in v:
        y.append(f(v_i))
    return y