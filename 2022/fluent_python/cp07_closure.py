
class Averager():
    def __init__(self):
        self.series = []
    def __call__(self, val):
        self.series.append(val)
        return sum(self.series)/len(self.series)

def make_averager():
    series = []
    def averager(val):
        series.append(val)
        return sum(series)/len(series)
    return averager

if __name__ == '__main__':
    print('use class')
    avg = Averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    
    print('use high order function')
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    print(avg.__code__.co_varnames)
    print(avg.__code__.co_freevars)
    print(avg.__closure__)
    print(avg.__closure__[0].cell_contents)
    
    