from functools import wraps
from collections import namedtuple

class DemoException(Exception):
    """An Exception type for the demonstration."""
    
def demo_exc_handling():
    print('-> coroutine started.')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run.')

Result = namedtuple('Result', 'count average')
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)

if __name__ == '__main__':
    c = demo_exc_handling()
    print(next(c))
    print(c.send(11))
    print(c.send(22))
    c.close()
    from inspect import getgeneratorstate
    print(getgeneratorstate(c))
    
    cc = averager()
    next(cc)
    print(cc.send(10))
    print(cc.send(20))
    print(cc.send(None))
