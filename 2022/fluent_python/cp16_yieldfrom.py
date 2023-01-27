from collections import namedtuple

Result = namedtuple('Result', 'count average')

# subgenerator
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

# delegating generator
def grouper(results, key):
    while True:
        results[key] = yield from averager()
        
# client code, caller
def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None) # important

    report(results)
    
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(':')
        print('{:2} {:5} averaging {:2f}{}'.format(
            result.count, group, result.average, unit))
        
data = {
    'girls:kg':
        [40.9, 38.5, 41.2],
    'girls:m':
        [1.6, 1.51, 1.44],
    'boys:kg':
        [50.9, 41.5, 48.2],
    'boys:m':
        [1.8, 1.61, 1.74],
}
        
if __name__ == '__main__':
    main(data)