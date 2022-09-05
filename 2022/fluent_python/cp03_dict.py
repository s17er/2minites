
def various_dict_def():
    a = dict(one=1, two=2, three=3)
    b = {'one':1, 'two':2, 'three':3}
    c = dict(zip(['one', 'two', 'three'], [1,2,3]))
    d = dict([('two', 2), ('three', 3), ('one', 1)])
    e = dict({'three':3, 'one':1, 'two':2})
    print(a == b == c == d == e)
    print(a)
    

if __name__ == '__main__':
    various_dict_def()