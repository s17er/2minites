import itertools
import operator

def vowel(c):
    return c.lower() in 'aeiou'

if __name__ == '__main__':
    # filter
    print(list(filter(vowel, 'Aardvark')))
    print(list(itertools.filterfalse(vowel, 'Aardvark')))
    print(list(itertools.dropwhile(vowel, 'Aardvark')))
    print(list(itertools.takewhile(vowel, 'Aardvark')))
    print(list(itertools.compress('Aardvark', (1,0,1,1,0,1))))
    print(list(itertools.islice('Aardvark', 4)))
    print(list(itertools.islice('Aardvark', 4, 7)))
    print(list(itertools.islice('Aardvark', 1, 7, 2)))
    
    # map
    sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
    print(list(itertools.accumulate(sample)))
    print(list(itertools.accumulate(sample, min)))
    print(list(itertools.accumulate(sample, max)))
    print(list(itertools.accumulate(sample, operator.mul)))
    print(list(itertools.accumulate(range(1, 11), operator.mul)))
    print(list(enumerate('albatroz', 1)))
    print(list(map(operator.mul, [0, 1, 2], [3, 4, 5]))) # 0*3, 1*4, 2*5
    print(list(map(lambda a, b: (a, b), [0, 1, 2], [3, 4, 5]))) 
    print(list(itertools.starmap(operator.mul, enumerate('albatroz', 1))))
    print(list(itertools.starmap(lambda a, b: b/a, enumerate(itertools.accumulate(sample), 1))))
    
    # merge
    print(list(itertools.chain('ABC', range(1, 3))))
    print(list(itertools.chain(enumerate('ABC'))))
    print(list(itertools.chain.from_iterable(enumerate('ABC'))))
    print(list(zip('ABC', 'DEF')))
    print(list(itertools.zip_longest('ABC', 'DEFHG', fillvalue='?')))
    print(list(itertools.product('ABC', 'DEF')))