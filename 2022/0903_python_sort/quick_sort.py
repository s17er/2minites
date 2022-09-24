from random import random
import time

def quick_sort(values):
    left = []
    right = []
    if len(values) <= 1:
        return values
    
    pibot = values[0]
    ref_count = 0
    
    for value in values:
        if value < pibot:
            left.append(value)
        elif value > pibot:
            right.append(value)
        else:
            ref_count += 1
            
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [pibot] * ref_count + right

def quick_sort_org(values):
    print('QUICK SORT ', values)
    _len = len(values)
    if _len == 1:
        return
    pibot = values[int(_len/2)]
    print('  pibot:', pibot)
    swap_count = 0
    ltarget = 0
    rtarget = _len - 1
    divide_index = 0
    while True:
        print('  loop start: pibot=', pibot, ' values=', values)
        while ltarget < _len:
            lval = values[ltarget]
            if lval >= pibot:
                break
            ltarget += 1
        while rtarget >= 0:
            rval = values[rtarget]
            if rval <= pibot:
                break
            rtarget -= 1

        print(f'  l={ltarget} r={rtarget}')

        if ltarget < rtarget:
            swap(values, ltarget, rtarget)
            divide_index = rtarget
            print('  SWAP POINT ', divide_index)
            swap_count += 1
        else:
            if lval == rval:
                print ('  END ', values)
                return
            else:
                # divide array
                print('  DIVIDE ', divide_index)
                quick_sort(values[0:divide_index]) # left values
                quick_sort(values[divide_index:]) # right values
    

def swap(list, i, j):
    _len = len(list)
    if i < _len and j < _len:
        list[i], list[j] = list[j], list[i]
    return list

def main_simple():
    floats = [8,4,5,2,1,9,0,7,3,6]
    t_start = time.perf_counter()
    print(floats)
    floats = quick_sort(floats)
    t_end = time.perf_counter()
    print(floats)
    t_diff = t_end - t_start
    print(f'{t_diff}s proceed.')
        
def main(n):
    floats = [random() for i in range(10**n)]
    t_start = time.perf_counter()
    print(floats[0])
    floats = quick_sort(floats)
    t_end = time.perf_counter()
    print(floats[0])
    t_diff = t_end - t_start
    print(f'{t_diff}s proceed.')
        
if __name__ == '__main__':
    main(5)
    #main_simple()