from random import random
import time

def selection_sort(targets):
    if not targets:
        return 
    
    for i in range(len(targets)):
        target = targets[i]
        min_index = i
        for j in range(i+1, len(targets)):
            if targets[j] < target:
                target = targets[j]
                min_index = j
        targets[i], targets[min_index] = targets[min_index], targets[i]
        

if __name__ == '__main__':
    floats = [random() for i in range(10**5)]
    t_start = time.perf_counter()
    print(floats[0])
    selection_sort(floats)
    t_end = time.perf_counter()
    print(floats[0])
    t_diff = t_end - t_start
    print(f'{t_diff}s proceed.')