from generators.middleSqureMethod import middleSquareMethod
from generators.modifiedSquareMethod import modifiedMiddleSquareMethod
from generators.lemerMethod import lemerMethod
from generators.multiplicativeCongruentialMethod import multiplicativeCongruentialMethod

def useMiddleSquareMethod():
    N = 6
    R0 = 0.583
    random_values = middleSquareMethod(R0, N)
    print(f"Базовая последовательность из {N} псевдослучайных чисел, сгенерированная методом серединных квадратов:", random_values)

def useModifiedMiddleSquareMethod():
    N = 6
    R0 = 0.5836
    R1 = 0.2176
    random_values = modifiedMiddleSquareMethod(R0,R1,N)
    print(f"Базовая последовательность из {N} псевдослучайных чисел, сгенерированная модифицированным методом серединных квадратов:", random_values)

def useLemerMethod():
    N = 5
    R0 = 0.585
    g = 927
    random_values = lemerMethod(R0, g, N)
    print(f"Базовая последовательность из {N} псевдослучайных чисел, сгенерированная методом Лемера:", random_values)

def useMultiplicativeCongruentialMethod():
    seed = 122
    a = 265
    m = 129
    N = 6
    random_values = multiplicativeCongruentialMethod(seed, a, m,N)
    print(f"Базовая последовательность из {N} псевдослучайных чисел, сгенерированная мультипликативным конгруэнтным методом:", random_values)

def main():
    print("1 задание")
    useMiddleSquareMethod()

    print("2 задание")
    useModifiedMiddleSquareMethod()
    
    print("3 задание")
    useLemerMethod()

    print("4 задание")
    useMultiplicativeCongruentialMethod()

main()