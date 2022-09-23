from functools import partial
from operator import mul

def main():
    # 引数が一部分だけ同じ呼び方をする際に利用できる
    print(mul(3, 7))
    triple = partial(mul, 3)
    print(triple(7))
    print(triple(8))
    print(triple(9))
    
    data = [
        ('Williams', 0, 'apple'),
        ('Ferrari', 2, 'car'),
        ('Mercedez', 1, 'bad'),
        ('Redbull', 0, 'bad'),
    ]
    
    from operator import itemgetter
    for d in sorted(data, key=itemgetter(1,0)):
        print(d)
        
    
    

if __name__ == '__main__':
    main()