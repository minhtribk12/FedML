import numpy as np

def zeros(n):
    if isinstance(n,int):
        sh = (n,n)
        return np.zeros(sh)
    elif isinstance(n,tuple):
        return np.zeros(n)
    else:
        return None