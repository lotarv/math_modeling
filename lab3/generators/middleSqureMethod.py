def middleSquareMethod(seed,N):
    result = [seed]

    current = seed

    for i in range(1, N+1):
        squared = current * current
        squared_str = f"{squared:.8f}".replace("0.","",-1)
        middle = squared_str[2:6]

        next = float(f"0.{middle}")

        result.append(next)
        current = next

    return result

