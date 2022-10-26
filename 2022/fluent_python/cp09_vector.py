from array import array
from math import hypot

class Vector2d:
    
    typecode = 'd'
    
    def __init__(self, x, y) -> None:
        self.x = float(x)
        self.y = float(y)
        
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
    
    def __format__(self, __format_spec: str = "") -> str:
        components = (format(c, __format_spec) for c in self)
        return '({}, {})'.format(*components)
    
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
    
    print(format(v))
    print(format(v, '.2f'))
    print(format(v, '.3e'))

