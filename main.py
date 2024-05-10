def main_fib(num):
    for i in range(num):
        print(fibbonaci(i))

def fibbonaci(num):
    if num == 1:
        return num
    elif num == 0:
        return num
    else:
        return fibbonaci(num-2) + fibbonaci(num -1)


main_fib(10)