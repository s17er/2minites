from array import array
import reprlib
import math

class Vector:
    
    typecode = 'd'
    
    def __init__(self, components) -> None:
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)
        
    def __repr__(self) -> str:
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)
    
    def __str__(self) -> str:
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self) -> float:
        return math.sqrt(sum(x * x for x in self))
    
    def __bool__(self) -> bool:
        return bool(abs(self))
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
    
if __name__ == '__main__':
    v = Vector([3.0, 4.0, 5.0, 6,0, 7.0, 8.0, 10.0])
    print(v)
    print(repr(v))