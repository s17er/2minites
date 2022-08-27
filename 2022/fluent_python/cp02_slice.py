
def main():
    s = 'bicycle'
    print(s[::3]) # 'bye'
    print(s[::-1]) # 'elcycib' <- reverse
    print(s[::-2]) # 'eccb'
    
def invoice():
    data = """
0.....6.................................40..........52.55.......
1909  Williams Renault                        $175.5  3   $577.5
3789  McLaren Mercedez                        $248.1  1   $248.1
1978  Ferrari                                 $200.0  2   $400.0
2022  Redbull Honda                           $512.1  5  $2560.5
    """
    NO = slice(0,6)
    TEAM = slice(6,40)
    UNIT = slice(40,52)
    QUANTITY = slice(52,55)
    TOTAL = slice(55,None)
    items = data.split('\n')[2:]
    for item in items:
        print(item[UNIT], item[TEAM])

if __name__ == '__main__':
    invoice()