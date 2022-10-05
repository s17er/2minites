from functools import reduce
from operator import mul

promos = set()

def promotion(active=True):
    def deco(func):
        print('running register(active=%s)->decorate(%s)' % (active, func))
        if active:
            promos.add(func)
        else:
            promos.discard(func)
        return func # require to return function
    return deco

@promotion(active=True)
def total(l):
    return sum(l)

@promotion(active=True)
def multi(l):
    return reduce(mul, l)
    
@promotion(active=False)
def average(l):
    return sum(l) / len(l)

def best_promo(l):
    return max(promo(l) for promo in promos)

if __name__ == '__main__':
    print(best_promo([1,2,3]))
    print(best_promo([2,-2,-3]))