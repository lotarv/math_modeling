def multiplicativeCongruentialMethod(seed, a, m, N):
    result = []
    x = seed

    for i in range(0, N):
        x = (a * x) % m
        result.append(float(x) / float(m))
    
    return result
