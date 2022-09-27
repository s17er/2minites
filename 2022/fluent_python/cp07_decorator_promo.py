from functools import reduce
from operator import mul

promos = []

def promotion(func):
    promos.append(func)
    return func # require to return function

@promotion
def total(l):
    return sum(l)

@promotion
def multi(l):
    return reduce(mul, l)
    
@promotion
def average(l):
    return sum(l) / len(l)

def best_promo(l):
    return max(promo(l) for promo in promos)

if __name__ == '__main__':
    print(best_promo([1,2,3]))
    print(best_promo([2,-2,-3]))