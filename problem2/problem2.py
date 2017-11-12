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


def findEven():
    pass