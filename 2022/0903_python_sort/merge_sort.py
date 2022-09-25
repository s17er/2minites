from random import random
import time

def merge_sort(values):
    _len = len(values)
    if _len <= 1:
        return values
    i = int(len(values)/2)
    left = merge_sort(values[0:i])
    right = merge_sort(values[i:])
    merge = []
    while True:
        if len(left) == 0:
            merge.extend(right)
            break
        if len(right) == 0:
            merge.extend(left)
            break

        if left[0] < right[0]:
            merge.append(left.pop(0))
        else:
            merge.append(right.pop(0))
    return merge
            

def main_simple():
    floats = [8,4,5,2,1,9,0,7,3,6]
    t_start = time.perf_counter()
    print(floats)
    floats = merge_sort(floats)
    t_end = time.perf_counter()
    print(floats)
    t_diff = t_end - t_start
    print(f'{t_diff}s proceed.')
        
def main(n):
    floats = [random() for i in range(10**n)]
    t_start = time.perf_counter()
    print(floats[0])
    floats = merge_sort(floats)
    t_end = time.perf_counter()
    print(floats[0])
    t_diff = t_end - t_start
    print(f'{t_diff}s proceed.')
        
if __name__ == '__main__':
    print('MERGE SORT')
    main(5)
    #main_simple()