def decode_str(s):
    for codec in ['utf_8', 'utf_16', 'shift_jis', 'euc-jp']:
        print(codec, s.encode(codec), sep='\t')

def multibyte_val():
    あいうえお = "aiueo"
    print(あいうえお)

if __name__ == '__main__':
    decode_str('白蛇大蛇')
    multibyte_val()