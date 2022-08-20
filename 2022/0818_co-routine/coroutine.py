from functools import wraps

def coroutine(f):
    @wraps(f)
    def primer(*args, **kwargs):
        g = f(*args, **kwargs)
        next(g)
        return g
    return primer

"""
    y = yes()
    print(next(y))
"""
def yes():
    while True:
        yield 'yes'
        
"""
    receiver = recv()
    next(receiver)
    receiver.send("1")
    receiver.send("2")
    receiver.send("3")
"""
def recv():
    print('start.')
    while True:
        v = yield
        print(f'received: {v}')
        
"""
    receiver = recv2()
    receiver.send("1")
    receiver.send("2")
    receiver.send("3")
"""
@coroutine
def recv2():
    print('start.')
    while True:
        v = yield
        print(f'received: {v}')
        
        
"""
    c = counter()
    c.send(1)
    c.send(2)
    c.send(3)
    try:
        c.send(None)
    except StopIteration as e:
        res = e.value
    res
"""
@coroutine
def counter():
    count = 0
    while True:
        by = yield
        if by is None:
            break
        count += by
    return count

if __name__ == '__main__':
    c = counter()
    c.send(1)
    c.send(2)
    c.send(3)
    try:
        c.send(None)
    except StopIteration as e:
        res = e.value
    print(res)