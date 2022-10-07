from re import A


def alias_check():
    a = {'name':'Mike', 'age':32}
    b = a
    print(a == b)
    print(a is b)
    c = {'name':'Mike', 'age':32}
    print(a == c)
    print(a is c)
    

if __name__ == '__main__':
    alias_check()