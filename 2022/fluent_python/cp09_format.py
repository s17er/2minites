# Show Python reference 6.1. string -- Common string operations
from datetime import datetime

if __name__ == '__main__':
    brl = 1/2.43
    print(brl)
    print(format(brl, '0.4f'))
    print('1 BRL = {rate:0.2f} USD'.format(rate=brl))
    
    print(format(42, 'b'))
    print(format(2/3, '.1%'))
    
    now = datetime.now()
    print(format(now, '%H:%M:%S'))
    print("It's now {:%I:%M %p}".format(now))
    print("It's now {date:%I:%M %p}".format(date=now))
    print("It's now {:%I:%M %p}. {}".format(now, 'dummy'))
    #print("It's now {:%I:%M %p}".format("dummy")) # ValueError: Invalid format specifier