from random import random
import time
import heapq

def heap_sort(items):
    h = []
    ret = []
    for item in items:
        heapq.heappush(h, item)
    while True:
        try:
            item = heapq.heappop(h)
            ret.append(item)
        except IndexError:
            break
        
    return ret
        


def main(n):
    floats = [random() for i in range(10**n)]
    t_start = time.perf_counter()
    print(floats[0])
    result = heap_sort(floats)
    t_end = time.perf_counter()
    print(result[0])
    t_diff = t_end - t_start
    print(f'{t_diff}s proceed.')
        
def main_min():
    floats = [8,4,5,2,1,9,0,7,3,6]
    t_start = time.perf_counter()
    print(floats)
    result = heap_sort(floats)
    t_end = time.perf_counter()
    print(result)
    t_diff = t_end - t_start
    print(f'{t_diff}s proceed.')

if __name__ == '__main__':
    print('HEAP SORT')
    main(5)