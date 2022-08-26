import os

def main():
    _, filename = os.path.split('/home/s17er/.ssh/idrsa.pub')
    print(_)
    print(filename)
    
    a, b = ret_tuple()
    print('---')
    print(a)  
    print(b)  
    
    print('---')
    print(divmod(20,8))
    t = (20,8)
    print(divmod(*t))
    
    
    print('---')
    a, b, *rest = range(5)
    print(a)  
    print(b)  
    print(rest)  

    print('---')
    metro_areas = [
        ('Tokyo', 'JP', 36.9, (35.6, 139.6)),
        ('Delhi', 'IN', 21.9, (28.6, 77.2)),
        ('NewYork', 'US', 20.1, (40.8, -74.0)),
        ('Sao Paulo', 'BR', 19.6, (-23.4, -46.6)),
    ]
    print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
    fmt = '{:15} | {:9.4f} | {:9.4f}'
    for name, cc, pop, (lat, lon) in metro_areas:
        print(fmt.format(name, lat, lon))

def ret_tuple():
    return (1, 2)

if __name__ == '__main__':
    main()