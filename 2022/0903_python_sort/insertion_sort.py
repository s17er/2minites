from random import random
import time

def insertion_sort(baselist):
    l = baselist
    length = len(baselist)
    for i in range(length):
        l = _insertion_sort(l, i)
    return l

def _insertion_sort(baselist, index=0):
    target_len = len(baselist)
    if target_len == index:
        return baselist

    target = baselist[index]
    for i in range(index):
        if target < baselist[i]:
            baselist = swap(baselist, i, index)
            break
    return baselist
    
    
    
def swap(baselist, insert_index, cut_index):
    is_end = (len(baselist) == cut_index + 1)
    l = []
    l.extend(baselist[:insert_index])
    l.append(baselist[cut_index])
    l.extend(baselist[insert_index:cut_index])
    if not is_end:
        l.extend(baselist[cut_index+1:])
    return l
    
def main(n):
    floats = [random() for i in range(10**n)]
    t_start = time.perf_counter()
    print(floats[0])
    result = insertion_sort(floats)
    t_end = time.perf_counter()
    print(result[0])
    t_diff = t_end - t_start
    print(f'{t_diff}s proceed.')
        
def main_min():
    floats = [random() for i in range(10**1)]
    t_start = time.perf_counter()
    print(floats)
    result = insertion_sort(floats)
    t_end = time.perf_counter()
    print(result)
    t_diff = t_end - t_start
    print(f'{t_diff}s proceed.')

if __name__ == '__main__':
    main(5)