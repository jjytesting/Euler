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


def evenSumFibonacci(fibo):
    evenSum = 0
    for item in fibo:
        if item % 2 == 0:
            evenSum += item
    return evenSum


def fibonacciRecursive(num):
    if num == 0:
        return 1
    elif num == 1:
        return 2
    else:
        return fibonacciRecursive(num - 1) + fibonacciRecursive(num - 2)


def getMaxNumFromFibonacci(fibo):
    return fibo.pop()


def fibonacciBeforeMax(maxNum):
    result = 0
    num = 0
    while (result < maxNum):
        num = num + 1
        result = getMaxNumFromFibonacci(fibonacci(num))
    return fibonacci(num - 1)


def fibonacciBeforeMaxWithoutRepeat(maxNum):
    fibo = []
    fibo.append(1)
    fibo.append(2)
    i = 1
    while (fibo[i] < maxNum):
        i = i + 1
        fibo.append(fibo[i - 1] + fibo[i - 2])
    return fibo[:i]


print(evenSumFibonacci(fibonacciBeforeMax(4000000)))


def fibonacciListComprehension(index):
    fibo = []
    if index == 0:
        fibo.append(0)
    elif index == 1:
        fibo = fibonacciListComprehension(0)
        fibo.append(1)
    elif index > 1:
        fibo =  fibonacciListComprehension(1) + [fibonacciListComprehension(x - 1)[- 1] + 
                fibonacciListComprehension(x - 2)[- 1] for x in range(2, index + 1)]
    return fibo


print(fibonacciListComprehension(10))


def fibonacciGenerator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


def makeFibo(maxNum):
    itr = fibonacciGenerator()
    fibo = []
    for i in itr:
        if i > maxNum:
            break
        else:
            fibo.append(i)
    return fibo

print(evenSumFibonacci(makeFibo(4000000)))




