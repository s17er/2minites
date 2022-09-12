from base64 import encode
import array

def str_byte_convert():
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
    
    
def octets():
    # create array of signed short int (16bit)
    numbers = array.array('h', [-2, -1, 0, 1, 2])
    octets = bytes(numbers)
    print(octets)
    
    # create array of unsigned int (32bit on Mac) 
    numbers = array.array('I', [20, 15, 0, 1, 2])
    print(numbers.itemsize)
    octets = bytes(numbers)
    print(octets)
    
    # create array of unsigned long (64bit on Mac)
    numbers = array.array('L', [20, 15, 0, 1, 2])
    print(numbers.itemsize)
    octets = bytes(numbers)
    print(octets)
    
if __name__ == '__main__':
    str_byte_convert()
    octets()
