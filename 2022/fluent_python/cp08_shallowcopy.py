def shallow_copy():
    l1 = [3, ['a', 'b'], (7, 8, 9)]
    l2 = list(l1)
    print(l2)
    print(l1 == l2) # True
    print(l1 is l2) # False
    
    l1.append(100)
    l1[1].remove('a')
    print(l1)
    print(l2)
    
    l2[1] += [33, 22]
    l2[2] += (10, 11)
    print(l1)
    print(l2)

    
if __name__ == '__main__':
    shallow_copy()