import time

'''
BAD Implement
Wait forever
'''
def fib(n):
    if n == 2 or n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
    
'''
GOOD Implement
'''
def fib2(n):
    if n == 2 or n == 1:
        return 1
    a,b = 1,1
    for i in range(n-2):
        a,b = a+b,a
    return a

def main():
    time_sta = time.perf_counter()
    print(fib2(1000))
    time_end = time.perf_counter()
    tim = time_end - time_sta
    print(tim)
    
if __name__ == '__main__':
    main()