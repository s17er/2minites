import random

class BingoCage:
    
    def __init__(self, items) -> None:
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
        
    def __call__(self) -> object:
        return self.pick()


if __name__ == '__main__':
    bingo = BingoCage(range(300))
    print(bingo.pick())
    print(bingo())
    print(callable(bingo))