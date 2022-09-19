import imp


def sort_reverse():
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'rasberry', 'banana']
    print(sorted(fruits, key=len))
    print(sorted(fruits, key=reverse))

def reverse(word):
    return word[::-1]

def map_alter():
    # These results are same.
    print(list(map(factorial, range(6))))
    print([factorial(x) for x in range(6)])
    
def filter_alter():
    # These results are same.
    print(list(map(factorial, filter(lambda x: x % 2, range(6)))))
    print([factorial(x) for x in range(6) if x % 2])

def reduce_alter():
    from functools import reduce
    from operator import add
    print(reduce(add, range(100)))
    print(sum( range(100)))

def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n-1)

if __name__ == '__main__':
    #sort_reverse()
    map_alter()
    filter_alter()
    reduce_alter()