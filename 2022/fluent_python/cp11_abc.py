import random
import abc

class Tombola(abc.ABC):
    
    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable."""
        
    @abc.abstractmethod
    def pick(self):
        """Remove item at random, returning it.
        
        This method should raise 'LookupError' when the instance is empty.
        """
        
    def loaded(self):
        """Return `True` if there's at least 1 item, `False` otherwise."""
        return bool(self.inspect())
    
    def inspect(self):
        """Return a sorted tuple with the items currently inside."""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))
    
class BingoCage(Tombola):
    
    def __init__(self, items) -> None:
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)
        
    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)
        
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
        
    def __call__(self):
        self.pick()


if __name__ == '__main__':
    cage = BingoCage(range(100))
    while True:
        try:
            print(cage.pick())
        except LookupError:
            break

