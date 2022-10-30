from array import array
from math import hypot
import math

class Vector2d:
    
    __slots__ = ('__x', '__y')
    typecode = 'd'
    
    def __init__(self, x, y) -> None:

        # protect variants
        self.__x = float(x)
        self.__y = float(y)
        
        # private variants (called most Pythonista)
        self._z = 0 # ' _z in __dict__'
        
        self.s = 0 # 's in __dict__'

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
        
    def angle(self):
        return math.atan2(self.y, self.x)
        
    def __iter__(self):
        return (i for i in (self.x, self.y))
        
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self) -> str:
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __bool__(self) -> bool:
        return bool(abs(self))
    
    def __abs__(self) -> float:
        return hypot(self.x, self.y)
    
    def __add__(self, target) -> object:
        x = self.x + target.x
        y = self.y + target.y
        return Vector2d(x, y)
    
    def __mul__(self, scalar) -> object:
        return Vector2d(self.x * scalar, self.y * scalar)
    
    def __format__(self, fmt_spec: str = "") -> str:
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)
    
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)
    
if __name__ == '__main__':
    v = Vector2d(5, 10)
    print(v.x, v.y)
    x, y = v
    print(x, y)

    print(repr(v))
    v_clone = eval(repr(v))
    print(v_clone == v)
    
    octets = bytes(v)
    print(octets)
    
    print(abs(v))
    print(bool(v), bool(Vector2d(0,0)))
    
    # format
    print(format(v))
    print(format(v, '.2f'))
    print(format(v, '.3e'))
    print(format(v, 'p'))
    print(format(v, '.3ep'))
    
    v1 = Vector2d(3, 4)
    v2 = Vector2d(2, 5)
    print(hash(v1))
    print(hash(v2))
    s = set([v1, v2])
    print(s)
    
    print(v1.__dict__)
    print(v1._Vector2d__x)
    
    

