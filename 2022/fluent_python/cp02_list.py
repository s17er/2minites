
def codepoints(symbols):
    return [ord(symbol) for symbol in symbols]

def cp_filter(symbols):
    return list(filter(lambda x: x % 2 == 0, map(ord, symbols) ))

if __name__ == '__main__':
    symbols = "あかさたな！"
    print(codepoints(symbols))
    print(cp_filter(symbols))
