
def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i
            
def chain2(*iterables):
    for i in iterables:
        yield from i
            
if __name__ == '__main__':
    s = 'ABC'
    t = tuple(range(3))
    print(list(chain(s, t)))
    print(list(chain2(s, t)))