from collections import namedtuple

def main():
    # 1st arg: Class name
    # 2nd arg: Field name (split by space)
    City = namedtuple('City', 'name country population coordinates')
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    print(tokyo)
    print(tokyo.population)
    print(tokyo[1])
    print(tokyo._fields)
    
    LatLong = namedtuple('LatLong', 'lat long')
    delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613899, 77.208889))
    print(delhi_data)
    
    delhi = City._make(delhi_data)
    print(delhi)
    print(delhi._asdict())
    
    

if __name__ == '__main__':
    main()