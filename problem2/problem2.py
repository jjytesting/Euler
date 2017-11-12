def fibonacci(num):
    fibo = []
    for i in range(num):
        if i == 0:
            fibo.append(1)
        elif i == 1:
            fibo.append(2)
        else:
            fibo.append(fibo[i - 1] + fibo[i - 2])
    return fibo


def evenFibonacciSum():
    fibo = []
    evenSum = 0
    i = 2
    fibo.append(1)
    fibo.append(2)
    evenSum = 2
    while fibo[i-1] < 4000000:
        fibo.append(fibo[i - 1] + fibo[i - 2])
        if fibo[i] % 2 == 0:
            evenSum += fibo[i]
        i += 1
    return evenSum
