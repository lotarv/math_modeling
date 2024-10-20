import math
import matplotlib.pyplot as plt
import numpy as np

#Функция для вычисления значений y для графика для линейной функции y = a * x + b
def linealFunc(a, arrX, b):
    arrX = np.array(arrX) 
    return np.array(np.round(a * arrX + b,2))

#Функция для вычисления значений y для графика для степенной функции y = b * x ^ a
def powerFunc(a, x,b):
    x = np.array(x) 
    return np.array(np.round(b * pow(x, a), 2))

#Функция для вычисления значений y для графика для экспоненциальной функции y = b * e ^(a * x)
def exponentialFunc(a, x,b):
    x = np.array(x) 
    return np.array(np.round(b * pow(math.e, x *a), 2))

#Функция для вычисления значений y для графика для линейной функции y = a * x^2 + b * x + c
def sqrFunc(a, x, b, c):
    x = np.array(x) 
    return np.array(np.round(a * pow(x,2) + b * x + c, 2))

#Функция для вычисления суммы элементов последовательности
def sumCoeff(arr):
    sum = 0
    for item in arr:
        sum += item
    return sum

#Функция для вычисления суммы квадратов элементов последовательности
def sumSqrCoeff(arr):
    sum = 0
    for item in arr:
        sum += (item*item)
    return sum

#Функция для вычисления суммы кубов элементов последовательности
def sumThreeCoeff(arr):
    sum = 0
    for item in arr:
        sum += pow(item, 3)
    return sum

#Функция для вычисления суммы элементов в 4 степени последовательности
def sumFourCoeff(arr):
    sum = 0
    for item in arr:
        sum += pow(item, 4)
    return sum

#Функция для вычисления суммы элементов двух последовательностей
def sumCoeffTwoArr(arrXi, arrYi):
    sum = 0
    for i in range(6):
        sum += arrXi[i] * arrYi[i]
    return sum

#Функция для вычисления суммы квадратов элементов двух последовательностей

def sumCoeffSqrTwoArr(arrXi, arrYi):
    sum = 0
    for i in range(6):
        sum += pow(arrXi[i],2) * arrYi[i]
    return sum

#Функция для вывода значений массива

def printArr(arr):
    for item in arr:
        print(item, end=", ")

#Функиця, которая логарифмирует элементы массива

def lnArr(arr):
    resultArr = []
    for item in arr:
        resultArr.append(math.log(item))
    return resultArr

#Функция для подсчета погрешности функций

def countInaccuracy(originalArr, newArr):
    sum = 0
    for i in range(len(originalArr)):
        sum += pow((originalArr[i] - newArr[i]), 2)
    return sum

#Функция для нахождения коэффициентов различных функций с помощью
#метода наименьших коэффициентов и метода Крамера
def findCoeff(arrXi, arrYi, type):
    n = len(arrXi)

    if type != 4:
        arrCoeff= [sumCoeff(arrXi), sumCoeff(arrYi), sumCoeffTwoArr(arrXi, arrYi), sumSqrCoeff(arrXi)]

        delta = arrCoeff[3] * n - arrCoeff[0] * arrCoeff[0]
        delta1 = arrCoeff[2] * n - arrCoeff[1] * arrCoeff[0]
        delta2 = arrCoeff[3] * arrCoeff[1] - arrCoeff[2] *  arrCoeff[0]

        a = round(delta1 / delta, 2)
        b = round(delta2 / delta, 2)
        c = 0

    else:
        arrCoeff= [sumFourCoeff(arrXi), sumThreeCoeff(arrXi), sumSqrCoeff(arrXi), sumCoeff(arrXi), sumCoeffSqrTwoArr(arrXi, arrYi), sumCoeffTwoArr(arrXi, arrYi), sumCoeff(arrYi)]
        delta = arrCoeff[0] * arrCoeff[2] * n + 2 * arrCoeff[1] * arrCoeff[2] * arrCoeff[3] - pow(arrCoeff[2], 3) - pow(arrCoeff[1],2) * n - pow(arrCoeff[3],2) * arrCoeff[0]
        delta1 = arrCoeff[4] * arrCoeff[2] * n + arrCoeff[5] * arrCoeff[2] * arrCoeff[3] + arrCoeff[1] * arrCoeff[3] * arrCoeff[6] - arrCoeff[6] * arrCoeff[2] * arrCoeff[2] - arrCoeff[5] * arrCoeff[1] * n - arrCoeff[3] * arrCoeff[3] * arrCoeff[4]
        delta2 = arrCoeff[0] * arrCoeff[5] * n + arrCoeff[1] * arrCoeff[2] * arrCoeff[6] + arrCoeff[2] * arrCoeff[3] * arrCoeff[4] - arrCoeff[5] * arrCoeff[2] * arrCoeff[2] - arrCoeff[4] * arrCoeff[1] * n - arrCoeff[0] * arrCoeff[3] * arrCoeff[6]
        delta3 = arrCoeff[0] * arrCoeff[2] * arrCoeff[6] + arrCoeff[1] * arrCoeff[3] * arrCoeff[4] + arrCoeff[2] * arrCoeff[1] * arrCoeff[5] - arrCoeff[4] * arrCoeff[2] * arrCoeff[2] - arrCoeff[1] * arrCoeff[1] * arrCoeff[6] - arrCoeff[0] * arrCoeff[3] * arrCoeff[5]

        a = round(delta1 / delta, 2)
        b = round(delta2 / delta, 2)
        c = round(delta3 / delta, 2)
    
    if type == 2 or type == 3:
        temp = pow(math.e, b)
        b = round(temp, 2)
    return a, b, c


# Вариант 9
# arrXi = [1, 5, 9, 13, 17, 21]
# arrYi = [2, 3.4, 4.2, 4.6, 5.2, 5.4]
arrXi = [1, 2, 3,4,5 , 6]
arrYi = [1, 1.5, 3.0, 4.5, 7, 8.5]
print("\nТаблица значений X:")
printArr(arrXi)
print("\n\nТаблица значений Y:")
printArr(arrYi)

linealA, linealB, c = findCoeff(arrXi, arrYi, 1)
print("\n\nЛинейная функция:")
if linealB >= 0:
    print(f"y = {linealA}x + {linealB}")
else:
    print(f"y = {linealA}x - {abs(linealB)}")

lnArrXi = lnArr(arrXi)
lnArrYi = lnArr(arrYi)
powerA, powerB, c = findCoeff(lnArrXi, lnArrYi, 2)
print("\nСтепенная функция:")
print(f"y = {powerB}x^{powerA}")

expA, expB, c = findCoeff(arrXi, lnArrYi, 3)
print("\nПоказательная функция:")
print(f"y = {expB}e^{expA}x")

sqrA, sqrB, sqrC = findCoeff(arrXi, arrYi, 4)
print("\nКвадратичная функция:")
if sqrB >= 0 and sqrC >= 0:
    print(f"y = {sqrA}x^2 + {sqrB}x + {sqrC}")
elif sqrB >= 0 and sqrC < 0:
    print(f"y = {sqrA}x^2 + {sqrB}x - {abs(sqrC)}")
elif sqrB < 0 and sqrC >= 0:
    print(f"y = {sqrA}x^2 - {abs(sqrB)}x + {sqrC}")
else:
    print(f"y = {sqrA}x^2 - {abs(sqrB)}x - {abs(sqrC)}")

# Погрешности

linealYi = linealFunc(linealA, arrXi, linealB)
powerYi = powerFunc(powerA, arrXi, powerB)
exponentialArrYi = exponentialFunc(expA, arrXi, expB)
sqrYi = sqrFunc(sqrA, arrXi, sqrB, sqrC)

linealS = round(countInaccuracy(arrYi, linealYi), 2)
powerS = round(countInaccuracy(arrYi, powerYi), 2)
exponentialS = round(countInaccuracy(arrYi, exponentialArrYi), 2)
sqrS = round(countInaccuracy(arrYi, sqrYi), 2)

print("\nПогрешности:")
print(f"Линейной функции: {linealS}")
print(f"Степенной функции: {powerS}")
print(f"Экспоненциальной функции: {exponentialS}")
print(f"Квадратичной функции: {sqrS}\n")

# Строим графики функций
plt.figure(figsize=(10, 6))

graphLinealYi = linealFunc(linealA, arrXi, linealB)
graphPowerYi = powerFunc(powerA, arrXi, powerB)
graphExponentialArrYi = exponentialFunc(expA, arrXi, expB)
graphSqrYi = sqrFunc(sqrA, arrXi, sqrB, sqrC)

plt.plot(arrXi, graphLinealYi, color="red", label="Линейная функция")
plt.plot(arrXi, graphPowerYi, color="blue", label="Степенная функция")
plt.plot(arrXi, graphExponentialArrYi, color="orange", label="Экспоненциальная функция")
plt.plot(arrXi, graphSqrYi, color="green", label="Квадратичная функция")
plt.scatter(arrXi, arrYi, color="black")
plt.scatter(arrXi, graphLinealYi, color="red")
plt.scatter(arrXi, graphPowerYi, color="blue")
plt.scatter(arrXi, graphExponentialArrYi, color="orange")
plt.scatter(arrXi, graphSqrYi, color="green")

plt.title('График точек x и y')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.legend()
plt.grid(True)
plt.show()

