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
        
if __name__ == '__main__':
    receiver = recv()
    next(receiver)
    receiver.send("1")
    receiver.send("2")
    receiver.send("3")