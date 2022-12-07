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
    
    # multiple
    print(list(itertools.islice(itertools.count(1, .3), 3)))
    print(list(itertools.islice(itertools.cycle("ABC"), 10)))
    print(list(itertools.islice(itertools.repeat("A"), 10)))
    
    # combinatoric generator
    # 長さが２となる要素の全組み合わせ
    print(list(itertools.combinations("ABC", 2)))
    # 重複を許す
    print(list(itertools.combinations_with_replacement("ABC", 2)))
    # すべての順列
    print(list(itertools.permutations("ABC", 2)))
    # デカルト積
    print(list(itertools.product("ABC", repeat=2)))
    
    # groupby
    print(list(itertools.groupby("LLLLAAGGG")))
    for c,group in itertools.groupby("LLLLAAGGG"):
        print(c, '->', list(group))
    animals = ['duck', 'eagle', 'rat', 'girafee', 'bear', 'bat', 'dolphin', 'shark', 'lion']
    animals.sort(key=len)
    print(animals)
    for c,group in itertools.groupby(animals, len):
        print(c, '->', list(group))
    for c,group in itertools.groupby(reversed(animals), len):
        print(c, '->', list(group))
    