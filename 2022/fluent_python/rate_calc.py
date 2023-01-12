
def calc(x1, x2, y1, y2, rate):
    i = 0
    sum_x = x1
    sum = x1 + y1
    current = float(sum_x / sum)
    while(current < rate):
        sum_x += x2
        sum += x2 + y2
        current = float(sum_x / sum)
        i += 1
    return i
    
if __name__ == '__main__':
    print(calc(519536, 546, 168160, 110, 0.76))
