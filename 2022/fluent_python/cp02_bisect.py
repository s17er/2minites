import bisect
import random

def main():
    l = [1, 3, 2, 6, 5, 7, 0, 9, 8]
    l.sort()
    print(bisect.bisect(l, 4))
    print(bisect.bisect_left(l, 4))
    bisect.insort(l, 4)
    print(l)
    
def grade(score, breakpoints=[60, 70, 80, 90], grades="EDCBA"):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

def random_insort():
    SIZE = 7
    random.seed(1789)
    l = []
    for i in range(SIZE):
        item = random.randrange(SIZE*2)
        bisect.insort(l, item)
        print('%2d ->' % item, l)
        

if __name__ == '__main__':
    main()
    print(grade(98))
    random_insort()