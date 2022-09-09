import random

def find_needle():
    ints = list(random.randint(0, 99) for i in range(10**5))
    print(set(ints))
    needles = [0,]
    print(len(set(needles) & set(ints)))
    

if __name__ == '__main__':
    find_needle()