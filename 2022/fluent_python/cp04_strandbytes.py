import re

re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r'\w+')
re_numbers_bytes = re.compile(rb'\d+')
re_words_bytes = re.compile(rb'\w+')


def re_str_bytes(text_str):
    text_bytes = text_str.encode('utf-8')
    print('Text', repr(text_str), sep='\n  ')
    print('Numbers')
    print('  str  :', re_numbers_str.findall(text_str))
    print('  bytes:', re_numbers_bytes.findall(text_bytes))
    print('Words')
    print('  str  :', re_words_str.findall(text_str))
    print('  bytes:', re_words_bytes.findall(text_bytes))
    
    

if __name__ == '__main__':
    s = "Ramanujan saw \u0be7\u0bed\u0be8\u0bef as 1729 = 1³ + 12³ = 9³ + 10³. "
    re_str_bytes(s)