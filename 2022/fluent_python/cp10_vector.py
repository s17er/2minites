from array import array
from curses.ascii import islower
import reprlib
import math
import numbers
import functools
import operator
import itertools

class Vector:
    
    typecode = 'd'
    shortcut_names = 'xyzt'
    
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
        # return tuple(self) == tuple(other) # overhead
        '''
        if len(self) != len(other):
            return False
        for a,b in zip(self, other):
            if a != b:
                return False
        return True
        '''
        # Pythonic!
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __abs__(self) -> float:
        return math.sqrt(sum(x * x for x in self))
    
    def __bool__(self) -> bool:
        return bool(abs(self))
        
    def __len__(self):
        return len(self._components)
        
    def __hash__(self) -> int:
        hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor, hashes, 0)
        
    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = f'{cls.__name__} indices must be integers'
            raise TypeError(msg)
            
    def __setattr__(self, name: str, value: float) -> None:
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attribute 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def __getattr__(self, name: str) -> float:
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has not attribute {!r}' # !r is repr()
        raise AttributeError(msg.format(cls, name))
    
    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n-1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a
        
    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))
    
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        componets = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(componets))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
    
if __name__ == '__main__':
    v = Vector([3.0, 4.0, 5.0, 6,0, 7.0, 8.0, 10.0])
    print(v)
    print(repr(v))
    print(len(v))
    print(v[3])
    print(v[1:4])
    #print(v['a']) #TypeError
    print(v[3:10])
    
    # access by attribute
    print(v.x)
    print(v.y)
    print(v.z)
    print(v.t)
    #print(v.a) # Attribute Error

    '''
    v.x = 10 # readonly
    print(v.x)
    print(v.a)
    print(repr(v))
    '''
    
    v1 = Vector([10.0, 4.0, 5.0, 6,0, 7.0, 8.0, 3.0])
    v2 = Vector([3.0, 4.0, 5.0, 6,0, 7.0, 8.0, 10.0])
    print(v1==v2)
    print(v==v2)

    print(format(v1, 'h'))
    print(format(v1, '.3eh'))
    print(format(v1, '.3e'))
    