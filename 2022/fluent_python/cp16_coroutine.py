
def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine recieved:', x)

def simple_coroutine2(a):
    print('-> started. a=', a)
    b = yield a
    print('-> recieved. b=', b)
    c = yield a + b
    print('-> recieved. c=', c)

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count

if __name__ == '__main__':
    '''
    c = simple_coroutine()
    print(c)
    next(c)
    c.send(42)
    '''

    '''
    c2 = simple_coroutine2(5)
    next(c2)
    print(c2.send(12))
    print(c2.send(32))
    '''

    c = averager()
    next(c)
    print(c.send(5))
    print(c.send(8))
