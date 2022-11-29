
def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')
    

if __name__ == '__main__':
    for c in gen_AB():
        print('--->', c)
        
    res1 = [x*3 for x in gen_AB()]
    print(res1)

    res2 = (x*3 for x in gen_AB()) # not tupple
    print(res2) # res2 is generator object.
    for i in res2:
        print('--->', i)