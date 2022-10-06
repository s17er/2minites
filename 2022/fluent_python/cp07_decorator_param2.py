import functools
import time

default_fmt = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=default_fmt):
    def decorate(func):
        def clocked(*_args):
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals())) # **locals() -> retrieve dict of all var in clocked()
            return _result
        return clocked
    return decorate

@clock()
def snooze(seconds):
    time.sleep(seconds)
        
@clock('{name}:{elapsed}')
def snooze2(seconds):
    time.sleep(seconds)
        

if __name__ == '__main__':
    for i in range(3):
        snooze(.123)
        snooze2(.123)