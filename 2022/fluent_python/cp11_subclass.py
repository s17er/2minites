from random import shuffle
import collections.abc

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck(collections.abc.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def __setitem__(self, position, card):
        self._cards[position] = card
    
    def __delitem__(self, position):
        del self._cards[position]
        
    def insert(self, position, value):
        self._cards.insert(position, value)
    
if __name__ == '__main__':
    deck = FrenchDeck()
    print(deck[:5])
    shuffle(deck)
    print(deck[:5])