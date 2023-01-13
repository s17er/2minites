
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

if __name__ == '__main__':
    '''
    c = simple_coroutine()
    print(c)
    next(c)
    c.send(42)
    '''

    c2 = simple_coroutine2(5)
    next(c2)
    print(c2.send(12))
    print(c2.send(32))

