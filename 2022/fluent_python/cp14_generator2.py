import re
import reprlib
from collections import abc

RE_WORD = re.compile(r'\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        '''
        for match in RE_WORD.finditer(self.text):
            yield match.group()
        '''
        return (match.group() for match in RE_WORD.finditer(self.text))
    
if __name__ == '__main__':
    s = Sentence('"The time has come, " the Walrus said,')
    print(s)
    for w in s:
        print(w)
    print(list(s))
    print(issubclass(Sentence, abc.Iterable)) 


