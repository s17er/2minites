
from math import hypot


class Vector:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
        
    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y})'
    
    def __bool__(self) -> bool:
        return bool(abs(self))
    
    def __abs__(self) -> float:
        return hypot(self.x, self.y)
    
    def __add__(self, target) -> object:
        x = self.x + target.x
        y = self.y + target.y
        return Vector(x, y)
    
    def __mul__(self, scalar) -> object:
        return Vector(self.x * scalar, self.y * scalar)
    
if __name__ == '__main__':
    v = Vector(5, 10)
    print(v)
    print(abs(v))
    print(Vector(3, 4) + Vector(6, 12))
    print(Vector(3, 4) * 4)
