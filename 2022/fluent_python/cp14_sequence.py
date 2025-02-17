import re
import reprlib
from collections import abc

RE_WORD = re.compile(r'\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
        
    def __getitem__(self, index):
        return self.words[index]
    
    def __len__(self):
        return len(self.words)
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
if __name__ == '__main__':
    s = Sentence('"The time has come, " the Walrus said,')
    print(s)
    for w in s:
        print(w)
    print(list(s))
    # behavior like iterable but Sentence is not subclass of Iterable.
    print(issubclass(Sentence, abc.Iterable)) 