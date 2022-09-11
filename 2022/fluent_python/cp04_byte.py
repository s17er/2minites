from base64 import encode


def main():
    s = 'café'
    print(len(s)) # 4length.
    b = s.encode('utf8')
    print(b) # b'caf\xc3\xa9 -> \x63\x61\x66\xc3\xa9
    print(len(b)) # 5bytes.
    print(b.decode('utf8'))
    print(b.decode('euc-jp')) # 文字化け
    
    print(b[:1]) # c
    print(b[:1].decode('utf8')) # c
    
    c = b'\x63\x61\x66\xc3\xa9'
    print(c.decode('utf8')) # café
    
    
if __name__ == '__main__':
    main()
