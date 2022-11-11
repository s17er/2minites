from random import shuffle
import collections
from typing import NamedTuple

#Card = collections.namedtuple('Card', ['rank', 'suit'])
#Card = collections.namedtuple('Card', 'rank suit')

class Card(NamedTuple):
    rank: str
    suit: str

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        '''
        c = [(rank, suit) for suit in self.suits for rank in self.ranks]
        print(c)
        '''
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def __setitem__(self, position, card):
        self._cards[position] = card
    
suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_value) + suit_value[card.suit]

if __name__ == '__main__':
    deck = FrenchDeck()
    print(deck[:5])
    shuffle(deck)
    print(deck[:5])