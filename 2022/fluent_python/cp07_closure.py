
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
        # 配列走査が走るので無駄が多い
        return sum(series)/len(series)
    return averager

def make_averager2():
    count = 0
    total = 0
    
    def avenger(val):
        nonlocal count, total
        count += 1
        total += val
        return total / count
    return avenger

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
    
    print('use high order function (nonlocal)')
    avg = make_averager2()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    print(avg.__code__.co_varnames)
    print(avg.__code__.co_freevars)
    print(avg.__closure__)
    print(avg.__closure__[0].cell_contents) # count
    print(avg.__closure__[1].cell_contents) # total
    