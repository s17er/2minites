from curses.ascii import isdigit
import unicodedata
import re

re_digit = re.compile(r'\d')

def print_unicode(s):
    for char in s:
        print('U+%04x' % ord(char),
                char.center(6),
                're_dig' if re_digit.match(char) else '-',
                'isdig' if char.isdigit() else '-',
                'isnum' if char.isnumeric() else '-',
                format(unicodedata.numeric(char), '5.2f'),
                unicodedata.name(char),
                sep='\t'
              )
    

if __name__ == '__main__':
    s = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'
    print_unicode(s)