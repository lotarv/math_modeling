import math
def fructionalPart(x):
    return x - math.floor(x)

def lemerMethod(seed, g, N):
    result = [seed]

    for i in range(1, N+1):
        result.append(fructionalPart(g * result[i-1]))
    
    return result
