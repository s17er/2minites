
b = 6
def f2(a):
    print(a)
    print(b)
    #b = 9 # this line occurs UnboundLocalError
    
def f3(a):
    global b
    print(a)
    print(b)
    b = 9 # global b

if __name__ == '__main__':
    f2(1)
    f3(1)
    f3(2)