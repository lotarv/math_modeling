def modifiedMiddleSquareMethod(R0,R1,N):
    result = [R0, R1]

    for i in range(2, N+1):
        squared = (result[i-1] + result[i-2]) * (result[i-1] + result[i-2])
        squared_str = f"{squared:.8f}".replace("0.","",-1)
        middle = squared_str[2:6]

        next = float(f"0.{middle}")

        result.append(next)
    
    return result

