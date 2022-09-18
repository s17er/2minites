
def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n-1)

def main():
    f = factorial
    print(f)
    print(f(5))
    print(list(map(factorial, range(10))))

if __name__ == '__main__':
    main()