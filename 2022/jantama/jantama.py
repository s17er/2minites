from collections import namedtuple

UMA = (
    ( # Syosin
        (35, 15, -5, -15),
        (35, 15, -5, -15),
        (35, 15, -5, -15),
    ),
    ( # Shi
        (55, 25, -5, -35),
        (55, 25, -5, -55),
        (55, 25, -5, -75),
    ),
    ( # Ketsu
        (95, 45, -5, -95),
        (95, 45, -5, -115),
        (95, 45, -5, -135),
    ),
    ( # Gou
        (125, 60, -5, -180),
        (125, 60, -5, -195),
        (125, 60, -5, -210),
    ),
    ( # Sei
        (125, 60, -5, -225),
        (125, 60, -5, -240),
        (125, 60, -5, -255),
    ),
)

def expected(rank, division, rate):
    per = list(map(lambda x: x/sum(rate), rate))
    uma = UMA[rank][division - 1]
    return sum([uma[i] * per[i] for i in range(4)])

    
    
def main():
    # janketu3
    #print(expected(2, 3, [30,25,19,26]))
    #print(expected(2, 3, [25.5,24,22.5,28]))
    print('G')
    print(expected(2, 3, [27,27,24,22]))
    
    print('My gold')
    print(expected(2, 3, [31.15,28.42,25.14,15.3]))
    my = [27.5,27.5,24,21]
    print('My gyoku')
    print(expected(3, 3, my))
    print(expected(4, 2, my))
    
    
if __name__ == '__main__':
    main()
