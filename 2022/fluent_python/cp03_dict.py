import collections

def various_dict_def():
    a = dict(one=1, two=2, three=3)
    b = {'one':1, 'two':2, 'three':3}
    c = dict(zip(['one', 'two', 'three'], [1,2,3]))
    d = dict([('two', 2), ('three', 3), ('one', 1)])
    e = dict({'three':3, 'one':1, 'two':2})
    print(a == b == c == d == e)
    print(a)
    
def dict_comprehension():
    CODES = [
       (5, "fly"),
       (1, "beta"),
       (0, "apple"),
       (8, "integer"),
    ]
    d = {word: num for num, word in CODES}
    print(d)
    d = {num: word.upper() for word, num in d.items() if num > 2}
    print(d)
    
def use_defaultdict():
    index = collections.defaultdict(list)
    index['a'] = [0,1,2]
    index['b'] = [3,4,5]
    print(index)
    l = ['a', 'b', 'c']
    for c in l:
        index[c].append(100)
    print(index)
    

if __name__ == '__main__':
    #various_dict_def()
    #dict_comprehension()
    use_defaultdict()